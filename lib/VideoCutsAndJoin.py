import ffmpeg
import subprocess

import os
from moviepy import VideoFileClip

class VideoCutsAndJoin:

	@staticmethod
	async def make_ts_cuts(file, start, end, fileOut, fileOutTs):
		try:
			# Создаем ОДИН входной поток
			inp = ffmpeg.input(file)
			
			# Обрезаем видео
			vid = inp.trim(start=start, end=end).setpts('PTS-STARTPTS')
			
			# Обрезаем аудио (берем поток из того же входа)
			# Используем a:0 (первый аудиопоток), чтобы явно указать, что берем
			audio = inp.audio.filter('atrim', start=start, end=end).filter('asetpts', 'PTS-STARTPTS')
			
			# Собираем выход. Убираем 'copy', указываем кодеки.
			# libx264 - стандартный кодек для mp4, aac - для звука.
			out = ffmpeg.output(
				vid, 
				audio, 
				fileOut, 
				vcodec='libx264', 
				acodec='aac',
				# Сбрасываем метаданные
				map_metadata='-1', 
				map_chapters='-1',
				# Чтобы видео сразу проигрывалось в браузере
				movflags='faststart' 
			)
			
			out.run(quiet=True)

		except ffmpeg.Error as e:
			print(f"FFmpeg не смог обработать файл '{file}' (от {start} до {end})")
			print(e.stderr.decode('utf-8', 'ignore'))
			return False

		command = [
			"ffmpeg",
			"-i", fileOut,
			"-c", "copy",
			"-bsf:v", "h264_mp4toannexb",
			"-f", "mpegts",
			fileOutTs
		]

		try:
			# check=True заставит Python выбросить исключение CalledProcessError, 
			# если ffmpeg завершится с ошибкой (ненулевой код возврата)
			await subprocess.run(command, check=True)
			print("Конвертация успешно завершена")
		except subprocess.CalledProcessError as e:
			print(f"Ошибка ffmpeg: Код возврата {e.returncode}")
		except FileNotFoundError:
			print("Ошибка: ffmpeg не установлен или не найден в PATH")

	@staticmethod
	def probe_file(fileIn): 
		try: 
			subprocess.run( 
				[
					"ffprobe", 
					"-v", 
					"error", 
					"-i", 
					fileIn
				], 
				check=True, 
				capture_output=True 
			) 
			return True 
		except	subprocess.CalledProcessError: 
			return False

	@staticmethod
	def concatenate_video_files(filesIn, fileOut):

		# file_temp_ts — список путей к .ts файлам
		# finalfile — путь к итоговому .mp4 файлу

		# Перемешиваем список
		# file_temp_ts = self.local_shuffle(options["filesIn"])
		file_temp_ts = filesIn

		# Формируем список аргументов для FFmpeg
		# Важно: FFmpeg требует, чтобы все файлы имели одинаковый формат и кодеки для concat
		command = [
			"ffmpeg",
			"-hide_banner", "-loglevel", "error", # Скрываем лишнюю информацию
			"-i", "concat:" + "|".join(file_temp_ts), # Собираем строку пайплайна только для аргумента -i
			"-c", "copy",
			"-bsf:a", "aac_adtstoasc",
			fileOut
		]

		print("Выполняется команда:", " ".join(command))

		try:
			# check=True выбросит исключение, если ffmpeg вернет ошибку
			subprocess.run(command, check=True)
			print(f"Файл успешно создан: {fileOut}")
		except subprocess.CalledProcessError as e:
			print(f"Ошибка FFmpeg (код {e.returncode}). См. логи выше.")
		except FileNotFoundError:
			print("Ошибка: FFmpeg не установлен или не найден в PATH.")


	@staticmethod
	def get_video_duration(fileIn):
		try:
			# Запускаем ffprobe и захватываем вывод
			result = subprocess.run(
				[
					"ffprobe",
					"-v", "error",
					"-show_entries", "format=duration",
					"-of", "default=noprint_wrappers=1:nokey=1",
					fileIn
				],
				capture_output=True, 
				text=True, 
				check=True
			)
			
			# Вывод приходит в виде строки, преобразуем в число
			duration = float(result.stdout.strip())
			return duration
			
		except (subprocess.CalledProcessError, ValueError):
			return None


	@staticmethod
	def append_audio_to_video(fileIn, audio, tempFolder, fileOut):
		# Проверяем существование исходного видео
		if not os.path.exists(fileIn):
			print(f"ERROR: Video file not found: {fileIn}")
			return
		
		if not audio:
			print("ERROR: Could not find a valid music file after several attempts.")
			return

		print(f"Selected: {audio}")

		try:			
			with VideoFileClip(fileIn) as clip:
				tempfile = tempFolder + "/final_sound.wav"
				audio_input = ffmpeg.input(audio)
				audio_cut = audio_input.audio.filter('atrim', duration=clip.duration)
				audio_output = ffmpeg.output(audio_cut, tempfile)
				ffmpeg.run(audio_output, quiet=True)
				print("audio trimmed")

				video = ffmpeg.input(fileIn)
				audio = ffmpeg.input(tempfile)

				ffmpeg.concat(video, audio, v=1, a=1).output(fileOut).run(quiet=True)
				print("audio added")
				print(f"Audio added successfully: {fileOut}")

		except ffmpeg.Error as e:
			print("FFMPEG ERROR:")
			print(e.stderr.decode() if e.stderr else "Unknown error")
		except Exception as e:
			print(f"General ERROR: {str(e)}")


