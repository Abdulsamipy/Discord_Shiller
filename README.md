## Discord Shill Bot

### Overview
This bot is designed to shill a predefined message on Discord channels. It utilizes the `discum` library to interact with Discord's API, allowing it to send messages to specified channels. The bot is intended for promotional purposes, specifically for shilling messages related to a tattoo shop and NFT art collection.

### Features
- Sends a custom message promoting "THE TATTOO SHOP" and its associated NFT art collection to designated Discord channels.
- Utilizes threading to efficiently send messages to multiple channels simultaneously.
- Allows for customization of the shilling message and supports embedding images and links.

### Usage
1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Customize the `message` variable in the script to tailor the shilling message to your needs.
5. Create text files containing Discord channel URLs where you want the message to be sent. Place these text files in the `Shilling_Channels` directory.
6. Each text file should contain one Discord channel URL per line.
7. Update the login credentials in the text file names within the `Shilling_Channels` directory. Each file name should follow the format: `username-token.txt`.
8. Run the script by executing `python shill_bot.py`.
9. The bot will start sending messages to the specified Discord channels.

