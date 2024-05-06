# Film-Finder

This script interacts with The Movie Database (TMDb) API to fetch data on movies or TV shows based on user input. Users can search by name, genre, release date, or rating, and the script will retrieve data accordingly. It also allows sorting the data based on title, vote average, or vote count, and generates a bar chart visualizing the vote average of the retrieved titles. The data is saved to an Excel file, which also includes the bar chart as an image.

Table of Contents:
1.Prerequisites
2.Running the Script
3.Modules
4.Features
5.Usage
6.Contributing

Prerequisites
Python 3.x
Required Python packages: requests, pandas, openpyxl, matplotlib
Obtain an API key from TMDb API.
You can install the required Python packages using:

pip install -r requirements.txt
Running the Script

To run the script, execute the Python file:

python script_name.py

You will be prompted for various inputs to perform the search. Follow the instructions provided by the script.

Modules
This script uses custom modules slicing and genre_id for processing and generating requests. Please refer to the script for more details on these modules.

Features
>Fetches data about movies or TV shows based on user input.
>Allows search by name, genre, release date, or rating.
>Allows sorting the data by title, vote average, or vote count.
>Saves the data to an Excel file, including a bar chart visualizing vote average by title.
Usage
The script will guide you through the process. Follow the prompts to enter your search preferences and sorting options.

Contributing
Contributions are welcome! Feel free to open an issue or pull request if you encounter any issues or have suggestions for improvements.
