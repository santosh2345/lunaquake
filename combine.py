import os

def delete_png_files(root_folder):
    for station_folder in os.listdir(root_folder):
        station_path = os.path.join(root_folder, station_folder)
        if os.path.isdir(station_path):
            for year_folder in os.listdir(station_path):
                year_path = os.path.join(station_path, year_folder)
                if os.path.isdir(year_path):
                    for day_folder in os.listdir(year_path):
                        day_path = os.path.join(year_path, day_folder)
                        if os.path.isdir(day_path):
                            for filename in os.listdir(day_path):
                                if filename.lower().endswith('.png'):
                                    file_path = os.path.join(day_path, filename)
                                    os.remove(file_path)
                                    print(f"Deleted: {file_path}")

if __name__ == "__main__":
    # Assuming you are currently in the 'plots' directory
    your_root_folder = os.getcwd()
    
    delete_png_files(your_root_folder)
