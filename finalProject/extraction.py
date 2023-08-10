

def process_video_batch(batch):
    import multiprocessing
    from mediapipe_extract import extraction
    with multiprocessing.get_context("spawn").Pool() as pool:
        pool.map(extraction, batch)


def process_videos(video_files, batch_size=4):
    for i in range(0, len(video_files), batch_size):
        batch = video_files[i:i+batch_size]
        process_video_batch(batch)


def main(video_dir):
    import os
    video_files = [file for file in os.listdir(video_dir) if file.endswith(".mp4")]
    process_videos(video_files, batch_size=4)
    print("All processes have finished.")


if __name__ == "__main__":
    video_dir = "/home/tester/finalProject/videos"
    main(video_dir)
