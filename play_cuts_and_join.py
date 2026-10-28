from lib.VideoCutsAndJoin import VideoCutsAndJoin

from lib.randomio import RandomIO

from predefined_vars import video_folders_zhszh
from predefined_vars import music_folders

# if __name__ == "__main__":

# get video files 
# get music files 
# get randomizer 
# get time or song by randomizer
# cicle 
# ? get random video by randomizer  
# ? cut one piece by random time
# ? cicle while time or song
# make ts files
# join files
# add audio 

import os
import random
from datetime import datetime

class VideoProcessor:
    def __init__(self, video_folders, music_folders, output_dir="./splits"):
        self.video_folders = video_folders
        self.music_folders = music_folders
        self.output_dir = output_dir
        
        # Создаем необходимые папки
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "ts"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "final"), exist_ok=True)

    def get_files_from_folders(self, folders, extensions):
        files = []

        for folder in folders:
            files.extend(RandomIO.files(folder, extensions))

        return files

    def local_random(self, items):
        """Безопасный выбор случайного элемента"""
        if not items:
            return None
        return random.choice(items)

    def process(self, target_duration_seconds=60):
        """Основной метод обработки"""
        
        # 1. Получаем списки файлов
        video_files = self.get_files_from_folders(self.video_folders, ['.mp4', '.mov', '.avi', '.mkv'])
        music_files = self.get_files_from_folders(self.music_folders, ['.mp3', '.wav', '.m4a'])

        if not video_files:
            print("ERROR: No video files found.")
            return
        if not music_files:
            print("ERROR: No music files found.")
            return

        print(f"Found {len(video_files)} videos and {len(music_files)} music tracks.")

        # 2. Выбираем случайную музыку
        music_track = self.local_random(music_files)
        print(f"Selected music: {music_track}")

        # 3. Цикл нарезки видео
        temp_ts_files = []
        accumulated_duration = 0
        
        while accumulated_duration < target_duration_seconds:
            video_file = self.local_random(video_files)
            
            # Получаем длительность исходного видео
            full_duration = VideoCutsAndJoin.get_video_duration(video_file)
            if not full_duration:
                print(f"Skipping file (cannot read duration): {video_file}")
                continue

            # Выбираем случайный сегмент (от 3 до 15 секунд, но не длиннее самого видео)
            seg_duration = random.uniform(3, min(15, full_duration))
            seg_start = random.uniform(0, full_duration - seg_duration)
            seg_end = seg_start + seg_duration

            # Формируем имена временных файлов
            base_name = f"seg_{len(temp_ts_files)}_{datetime.now().strftime('%H%M%S%f')}"
            mp4_temp = os.path.join(self.output_dir, f"{base_name}.mp4")
            ts_temp = os.path.join(self.output_dir, "ts", f"{base_name}.ts")

            # 4. Нарезаем сегмент
            print(f"Cutting {seg_duration:.2f}s from {os.path.basename(video_file)}")
            success = VideoCutsAndJoin.cut_video_segment(video_file, seg_start, seg_end, mp4_temp)

            if not success:
                print("Failed to cut segment, skipping.")
                continue

            # 5. Конвертируем в TS
            VideoCutsAndJoin.make_ts_file(mp4_temp, ts_temp)
            
            # Удаляем промежуточный .mp4, чтобы не засорять диск
            if os.path.exists(mp4_temp):
                os.remove(mp4_temp)

            if os.path.exists(ts_temp):
                temp_ts_files.append(ts_temp)
                accumulated_duration += seg_duration
            else:
                print(f"TS file was not created for {mp4_temp}")

        # 6. Склеиваем TS файлы
        if not temp_ts_files:
            print("ERROR: No video segments were created.")
            return

        joined_video_path = os.path.join(self.output_dir, f"joined_{datetime.now().strftime('%d%m%Y_%H%M%S')}.mp4")
        print(f"Concatenating {len(temp_ts_files)} segments...")
        VideoCutsAndJoin.concatenate_video_files(temp_ts_files, joined_video_path)

        # 7. Добавляем аудио
        final_output_path = os.path.join(self.output_dir, "final", f"FINAL_{datetime.now().strftime('%d%m%Y_%H%M%S')}.mp4")
        print("Adding audio track...")
        VideoCutsAndJoin.append_audio_to_video(joined_video_path, music_track, final_output_path)

        # 8. Очистка
        for f in temp_ts_files:
            if os.path.exists(f):
                os.remove(f)
        if os.path.exists(joined_video_path):
            os.remove(joined_video_path)

        print(f"\n--- PROCESS COMPLETE ---")
        print(f"Result saved to: {final_output_path}")


# --- Пример использования ---
if __name__ == "__main__":
    # Укажите здесь пути к вашим папкам

    processor = VideoProcessor(video_folders_zhszh, music_folders)
    
    # Собрать итоговое видео длиной примерно 60 секунд
    processor.process(target_duration_seconds=60)