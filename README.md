Art Web Shop

Welcome to Art Web Shop, a web application for managing and showcasing artworks and artist information. This application allows you to create a platform where artists can display their artwork, and users can browse, purchase, and interact with the art community.
Features

    Artwork Management: Easily add, update, and delete artworks, including details like title, description, price, and image.
    Artist Profiles: Create and manage artist profiles, showcasing their bio, portfolio, and contact information.
    User Authentication: Secure user registration and login system using JSON Web Tokens (JWT) for authentication and authorization.
    Order Management: Admins can handle and track orders, update order status, and manage inventory.
    Search and Filtering: Search for artworks by title, artist, or category, and apply filters based on various criteria.
    User Reviews and Ratings: Users can leave reviews and ratings for artworks, contributing to an interactive art community.

Installation

    Clone the repository:

    bash

git clone https://github.com/ka-tarina/Art-web-shop.git

Install the required dependencies:

bash

pip install -r requirements.txt

Configure the application settings:

    Create a .env file based on the provided .env.example file.
    Modify the configuration parameters in the .env file to match your environment (e.g., database connection details, authentication settings).

Run the application:

bash

    uvicorn main:app --reload

