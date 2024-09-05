import os
from datetime import datetime
from app import app, db
from models import Product, Category
import logging

# Set logging level
logging.basicConfig(level=logging.INFO)

def delete_existing_data():
    with app.app_context():
        logging.info("Deleting existing data...")
        Product.query.delete()
        Category.query.delete()
        db.session.commit()

def seed_categories():
    with app.app_context():
        logging.info("Seeding categories...")

        # Define example categories based on provided data
        categories_data = [
            {"id": 1, "name": "Men's Clothing", "description": "All types of men's clothes."},
            {"id": 2, "name": "Men's Shoes", "description": "All types of men's shoes."},
            {"id": 3, "name": "Men's Accessories", "description": "All types of men's accessories."},
            {"id": 4, "name": "Women's Clothing", "description": "All types of women's clothes."},
            {"id": 5, "name": "Women's Shoes", "description": "All types of women's shoes."},
            {"id": 6, "name": "Women's Accessories", "description": "All types of women's accessories."},
            {"id": 7, "name": "Accessories", "description": "All types of accessories."},
            {"id": 8, "name": "Clothes", "description": "All types of clothes."},
            {"id": 9, "name": "Shoes", "description": "All types of shoes."}
        ]

        # Create Category objects from the predefined data
        categories = [Category(id=cat["id"], name=cat["name"], description=cat["description"]) for cat in categories_data]

        # Clear existing categories and insert predefined categories
        db.session.query(Category).delete()
        db.session.bulk_save_objects(categories)
        db.session.commit()

        logging.info("Categories seeded.")
        return categories

def seed_products(categories):
    with app.app_context():
        logging.info("Seeding products...")

        # Define one example product for each category
        products_data = [
            {
                "name": " T-shirt",
                "image_url": "https://i.pinimg.com/236x/48/08/b3/4808b3e1ff6aa81f8298cb1e0fb4f73c.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
             {
                "name": "Official suits",
                "image_url": "https://i.pinimg.com/236x/1b/0f/a1/1b0fa16f3aca3bec8740bb42e8266c02.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
             {
                "name": "Hooded cardigan",
                "image_url": "https://i.pinimg.com/236x/73/1b/f1/731bf13ee11a8fbc2ba0cf22af565125.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
              {
                "name": "Casual wear",
                "image_url": "https://i.pinimg.com/236x/91/d1/e5/91d1e582f6a0e58c13513e0c2391f689.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
               {
                "name": "two-piece set",
                "image_url": "https://i.pinimg.com/236x/22/57/cc/2257ccd3f7ca68eb23bf2efc62b87e40.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
               {
                "name": "Casual fit",
                "image_url": "https://i.pinimg.com/236x/be/ab/1a/beab1aa1a525be760a13b1edb8649867.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Office Suit",
                "image_url": "https://i.pinimg.com/236x/e7/28/a4/e728a44e66d10ef160a1bb0cb82e290d.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Cargo jeans",
                "image_url": "https://i.pinimg.com/236x/98/4f/75/984f75d50b710a17a31ea78cb5f65fe5.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "African Suit",
                "image_url": "https://i.pinimg.com/236x/5b/73/f4/5b73f4ae6c20163de1bba48591ee9469.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
               {
                "name": "Jordan shorts",
                "image_url": "https://i.pinimg.com/236x/92/a0/96/92a096c0735b3bbab5b604222c5728af.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Shirts",
                "image_url": "https://i.pinimg.com/236x/dd/4d/23/dd4d238590224586912f475f26bf8db3.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Shirt",
                "image_url": "https://i.pinimg.com/236x/17/25/79/1725796373a23b7da4b299d6440f8586.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Basketball t-shirt",
                "image_url": "https://i.pinimg.com/236x/57/8b/1d/578b1dafbc1a0dc80e72a61a3791ea75.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Official Set",
                "image_url": "https://i.pinimg.com/236x/1a/b3/e6/1ab3e6038c13132d22cb6ad410edaeee.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "College jacket",
                "image_url": "https://i.pinimg.com/236x/36/84/cd/3684cdb6c819f360486e0b1b489167a0.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Pullover Hoodie",
                "image_url": "https://i.pinimg.com/236x/ec/48/7e/ec487ec339cacc808f02b7ec830ab2c7.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "College jacket",
                "image_url": "https://i.pinimg.com/236x/a0/ed/cc/a0edccbf676a1336d8b87ff007dc716b.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Cargo pant",
                "image_url": "https://i.pinimg.com/236x/fd/fb/d4/fdfbd402556530e5f212c0572d8b908a.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Jacket",
                "image_url": "https://i.pinimg.com/236x/df/54/f1/df54f1c46d54a67f29fbc76f8f57f74d.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Jacket",
                "image_url": "https://i.pinimg.com/236x/68/13/18/681318ad5853842723c62bd204f29dc4.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Leather Jacket",
                "image_url": "https://i.pinimg.com/236x/e7/3e/44/e73e4451edecebe1d7e5a17a5e9eb67a.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Cargo pants",
                "image_url": "https://i.pinimg.com/236x/0f/5a/4b/0f5a4b8f2265045cc4503c332d6042ae.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Hoodie",
                "image_url": "https://i.pinimg.com/236x/e4/da/12/e4da12050efdd1cb20bc0e536a0c7f06.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Cargo shorts",
                "image_url": "https://i.pinimg.com/236x/4f/33/20/4f33204abbbee5dcd1a0d1588b3135d5.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "T-Shirtvest",
                "image_url": "https://i.pinimg.com/236x/44/92/d2/4492d2dee35065d9556ed7be2f90e2c9.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Pullneck",
                "image_url": "https://i.pinimg.com/236x/b8/93/ce/b893ce81dc1c2810449d620e823c4069.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Hoodie",
                "image_url": "https://i.pinimg.com/236x/f0/c4/3d/f0c43dac9fb3255e5ecd1e58bb41dbd3.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "T-shirt",
                "image_url": "https://i.pinimg.com/236x/59/07/d1/5907d15cb579b44680044125e5ec8350.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "T-shirts",
                "image_url": "https://i.pinimg.com/236x/c9/83/90/c9839094fb8490c3fce03c4ad70fa117.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Sweatshirt",
                "image_url": "https://i.pinimg.com/236x/6c/79/80/6c7980d092560b779f480d5234dd9b48.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Denim jacket",
                "image_url": "https://i.pinimg.com/236x/36/7e/63/367e638332f2a3381d3dadeedee72b02.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "T-shirt",
                "image_url": "https://i.pinimg.com/474x/b8/1c/b0/b81cb0e66565da12efdb2cfe384680f3.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Black Denim trousers",
                "image_url": "https://i.pinimg.com/236x/5e/59/a1/5e59a172ec4d258a40cdff6811ea2ad0.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Pair of Trousers",
                "image_url": "https://i.pinimg.com/474x/70/ad/d3/70add3a7e405de9eccbf3a2c02756dfa.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Denim jacket",
                "image_url": "https://i.pinimg.com/236x/e8/d2/74/e8d274913a23579394a9375ed95eeeb4.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Ripped Jeans",
                "image_url": "https://i.pinimg.com/236x/13/42/87/134287fcdf70617901e03f64ba31c1df.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Ripped shorts",
                "image_url": "https://i.pinimg.com/originals/3b/3f/bd/3b3fbd0613e6b946e4c4023b0111fb8a.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Shorts",
                "image_url": "https://i.pinimg.com/474x/b2/55/b8/b255b8e4dd6fdb32c72ef09f76a52e42.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Denim cargos",
                "image_url": "https://i.pinimg.com/474x/88/60/1f/88601fce9a6852b2a119dd7fd5195644.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
                    {
                "name": "Rugged jeans",
                "image_url": "https://i.pinimg.com/236x/30/15/e6/3015e609989212aa2c9b516551918cba.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Knee-length jorts",
                "image_url": "https://i.pinimg.com/236x/c2/64/12/c26412543ccd465cb9d9db89a5b6002d.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Flunnels",
                "image_url": "https://i.pinimg.com/236x/6b/fc/ed/6bfcedbd9c254fbb47d6196a45b6298d.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Oversized sweatshirt",
                "image_url": "https://i.pinimg.com/236x/bf/e7/da/bfe7da7fa7bb4ba674628c94db63e91d.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Shirt",
                "image_url": "https://i.pinimg.com/236x/b0/a6/b8/b0a6b89d2eb821f49311578799e58dee.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Cotton jackets",
                "image_url": "https://i.pinimg.com/236x/26/5a/7a/265a7add90f5682fc56ad7ccb656fd01.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Official suits",
                "image_url": "https://i.pinimg.com/236x/20/20/8b/20208b2612c7da4421d0ddaf83132303.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Sweatshirt",
                "image_url": "https://i.pinimg.com/236x/1f/45/ae/1f45ae5aa38ddf3840c6661346c46860.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Wild cargos",
                "image_url": "https://i.pinimg.com/236x/52/3b/7f/523b7f48e0419bc9d03c47a0b6822276.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Puffer Jackets",
                "image_url": "https://i.pinimg.com/236x/28/e6/85/28e685cb61de87a3c3ce91a4f3c78054.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Sweater vests",
                "image_url": "https://i.pinimg.com/236x/7b/a9/9d/7ba99d4885c4c311be48dae1e6ee5c82.jpg",
                "description": "Comfortable clothes available in various colors.",
                "price": 19.99,
                "stock": 50,
                "category_id": 1  # Men's Clothing
            },
            {
                "name": "Running Shoes",
                "image_url": "https://i.pinimg.com/236x/8a/02/96/8a0296c50ddb2a8d889cbcb51e67ca45.jpg",
                "description": "High-performance running shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "TimberLand",
                "image_url": "https://i.pinimg.com/236x/cf/2c/de/cf2cde79541dd9841405615c744ecf7d.jpg",
                "description": "High-performance running shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "TimberLand",
                "image_url": "https://i.pinimg.com/236x/55/4d/a0/554da013a7af35397de6a8aa4da0d2a9.jpg",
                "description": "High-performance running shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Bloafers",
                "image_url": "https://i.pinimg.com/236x/a4/48/38/a44838914879e0ed44d2a5f599e59941.jpg",
                "description": "High-performance running shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Leather TimberLand",
                "image_url": "https://i.pinimg.com/236x/4f/87/8a/4f878a820f047e9a0211e95140559a8f.jpg",
                "description": "High-performance running shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Sneakers",
                "image_url": "https://i.pinimg.com/236x/dd/01/d2/dd01d290df426efd7aec681f8b1d6caa.jpg",
                "description": "High-performance running shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Sneakers",
                "image_url": "https://i.pinimg.com/236x/0e/f1/13/0ef113de4b877881bd328ee17f51f640.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 150,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Sporty Shoes",
                "image_url": "https://i.pinimg.com/236x/0c/87/4d/0c874d1ac037a18401b32c46e181bb9e.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 189.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Jake Davis Shoes",
                "image_url": "https://i.pinimg.com/236x/28/b1/eb/28b1eb78217a846c4eb10290672e63fb.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Sneakers",
                "image_url": "https://i.pinimg.com/236x/54/eb/44/54eb443df1e62da8f58f27fea8a947d1.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Puma Sneakers",
                "image_url": "https://i.pinimg.com/236x/ee/a9/e5/eea9e5ff452f294312f6804fc6b0fb16.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 89.99,
                "stock": 50,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Official shoes",
                "image_url": "https://i.pinimg.com/236x/b5/60/99/b560997015c40b31dadcb3aced5b5c15.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Official shoes",
                "image_url": "https://i.pinimg.com/236x/21/57/5b/21575ba4801a676ab6435a4a638ebd59.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
             {
                "name": "Official shoes",
                "image_url": "https://i.pinimg.com/236x/12/3c/7e/123c7e6135773ba4fb52d7a23ac2f4e4.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Slides",
                "image_url": "https://i.pinimg.com/originals/bd/46/52/bd4652033750db074eb0f9d52dfc445a.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
             {
                "name": "Official shoes",
                "image_url": "https://i.pinimg.com/236x/0b/ee/ad/0beead4382b623ad458a4befbde6d712.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
             {
                "name": "Slides",
                "image_url": "https://i.pinimg.com/236x/a1/a7/19/a1a719d445e39cc2c0c17901cd8a9351.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Loafers ",
                "image_url": "https://i.pinimg.com/236x/09/9a/0c/099a0cf63dc0e3ac367f931b839eb149.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
             {
                "name": "Caterpillar Spiro",
                "image_url": "https://i.pinimg.com/236x/51/54/08/51540820942bdd9daf2e833ca2e7b664.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
             {
                "name": "Slides",
                "image_url": "https://i.pinimg.com/236x/3e/19/5c/3e195cd5b4423d1d14001097c62ca2aa.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Sandals",
                "image_url": "https://i.pinimg.com/236x/35/b5/d7/35b5d752c6e62dc68c3ece21e1d69445.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Nike Slides",
                "image_url": "https://i.pinimg.com/236x/63/47/ac/6347acd53a8670b217accfc954d129bc.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Leather Boots",
                "image_url": "https://i.pinimg.com/236x/9c/d7/9d/9cd79d2c25582487798003720371b319.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Canvas",
                "image_url": "https://i.pinimg.com/236x/e2/65/9f/e2659f9e7273be6dc08285024862adf7.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Casual Slides",
                "image_url": "https://i.pinimg.com/236x/dc/d4/9c/dcd49c15cd335ab8f8bbdab8d67b68c8.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Wedges",
                "image_url": "https://i.pinimg.com/236x/ca/1b/94/ca1b945690cd0abf1cbf354fb93e356f.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Sandals",
                "image_url": "https://i.pinimg.com/236x/5b/7f/14/5b7f14a1eab222fb14fa625fd378dd0e.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Loafers",
                "image_url": "https://i.pinimg.com/236x/2e/6d/13/2e6d13fc0e2d91403e074d49cc9989f5.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Leather Boots",
                "image_url": "https://i.pinimg.com/236x/cf/f8/2e/cff82e57b6d4dfda35fbd29a12bfcd7d.jpg",
                "description": "High-performance shoes for all activities.",
                "price": 99.99,
                "stock": 120,
                "category_id": 2  # Men's Shoes
            },
            {
                "name": "Leather Belt",
                "image_url": "https://i.pinimg.com/236x/f4/de/33/f4de3353c4db98e57f83217ce98dd52f.jpg",
                "description": "Stylish leather belt with a classic buckle.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
             {
                "name": "Set of watch",
                "image_url": "https://i.pinimg.com/474x/27/7b/27/277b271fa5217e9f3feb87e469bb8d63.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Silver bracelet",
                "image_url": "https://i.pinimg.com/236x/de/5d/b9/de5db956252ec40975bc2f075179c5bd.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },   
            {
                "name": "stainless chain",
                "image_url": "https://i.pinimg.com/236x/63/5c/f9/635cf92967542f7e150277ae9a10ee69.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Sunglasses",
                "image_url": "https://i.pinimg.com/236x/da/db/fc/dadbfc473c954073f0107a0564dafa29.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Modern watch",
                "image_url": "https://i.pinimg.com/236x/d2/8b/31/d28b31dfb44be70f68456771da9e1e99.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Round glasses",
                "image_url": "https://i.pinimg.com/236x/d7/ed/59/d7ed59566eb2fcc970c120f40841384e.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Cross pendant",
                "image_url": "https://i.pinimg.com/236x/cb/49/57/cb4957b8a3fb616007aa572daf040531.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Rings",
                "image_url": "https://i.pinimg.com/236x/47/60/01/476001c4d6900ad26de5408770c4686a.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Marvin",
                "image_url": "https://i.pinimg.com/originals/b3/51/88/b351884ceff458a8632923b20103171b.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Sweatband",
                "image_url": "https://i.pinimg.com/originals/cb/5f/53/cb5f530ca59b4b49e414ef5f89c94351.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Caps",
                "image_url": "https://i.pinimg.com/236x/5b/c9/49/5bc949e23481d5209ccac03fe263a560.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "A cap",
                "image_url": "https://i.pinimg.com/236x/79/3b/c3/793bc362e7b44449dc97af568d76701b.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "A hat",
                "image_url": "https://i.pinimg.com/236x/87/33/00/873300d2d907151cf1b353bee17d13bf.jpg",
                "description": "Stylish accesory.",
                "price": 39.99,
                "stock": 50,
                "category_id": 3  # Men's Accessories
            },
            {
                "name": "Floral Dress",
                "image_url": "https://i.pinimg.com/236x/fd/8d/c2/fd8dc2507ec0796cf5a036474668cf2e.jpg",
                "description": "Elegant floral dress perfect for summer outings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "2-piece set",
                "image_url": "https://i.pinimg.com/236x/03/fa/05/03fa05297bd2edf802e7b60594e1ac51.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Bodysuits",
                "image_url": "https://i.pinimg.com/236x/8f/d2/34/8fd2345512dbff8ede50100747ba4ef8.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "3-piece set",
                "image_url": "https://i.pinimg.com/236x/f5/82/35/f58235411207991d9ea83d72aa29383c.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Fleece Hoodie",
                "image_url": "https://i.pinimg.com/236x/67/01/41/670141be9107a3ae1756c3825cf9bdcb.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Official pants",
                "image_url": "https://i.pinimg.com/236x/bc/39/75/bc3975a6532dbb17201c1b3b862ae269.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "flared floral pants",
                "image_url": "https://i.pinimg.com/236x/43/dd/bb/43ddbb86aec0e89b6365087f550086a3.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "sweatpants set",
                "image_url": "https://i.pinimg.com/236x/a7/44/45/a7444597a77e2fe7e41f7f423eca3dc2.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Print wide leg pants",
                "image_url": "https://i.pinimg.com/236x/1b/bd/77/1bbd7759e251e6efc4659aef2d1021c4.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Silk tank top",
                "image_url": "https://i.pinimg.com/236x/26/ae/26/26ae2697ce1f362fdb06c0402f704a2a.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Baggy Jeans",
                "image_url": "https://i.pinimg.com/236x/fc/b4/52/fcb4525891d549dab6f2b4d991396b74.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Official Jumpsuit",
                "image_url": "https://i.pinimg.com/236x/53/43/f9/5343f90cc95a4ef49b61e59ecdac30b3.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Summer dress",
                "image_url": "https://i.pinimg.com/236x/47/17/d7/4717d7787dc627e94f5c13e5ad356c3f.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Top",
                "image_url": "https://i.pinimg.com/236x/f9/57/4a/f9574a9cd1e0c04f1b37800bb53aaf48.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Pathwork jumpsuit",
                "image_url": "https://i.pinimg.com/236x/36/7f/b6/367fb6f0c5e2a009c50a783361c88ea0.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Cherry print dress",
                "image_url": "https://i.pinimg.com/474x/6e/d7/30/6ed7303d14b8a7feaa2644eb7630b980.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Body-con top",
                "image_url": "https://i.pinimg.com/236x/d4/15/6c/d4156c2a717a905bb15d2f0cc2520d7e.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Mummy Jeans",
                "image_url": "https://i.pinimg.com/236x/0c/80/27/0c80271b410fa539f37d610201828935.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Leather cargo pants",
                "image_url": "https://i.pinimg.com/236x/10/b0/84/10b084c422e8723555b5cb61044c1b8e.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Oversized hoodie",
                "image_url": "https://i.pinimg.com/236x/ae/2d/43/ae2d43f8436e6ebe1c1b8ecc5eb94c9e.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },

            {
                "name": "Scoop Neck t-shirt",
                "image_url": "https://i.pinimg.com/236x/7e/46/73/7e467331003efb80ee3045e5d7a5b663.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Gothic",
                "image_url": "https://i.pinimg.com/236x/de/9e/f0/de9ef0fda61b2310950775e253caadf4.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Cardigans",
                "image_url": "https://i.pinimg.com/236x/a7/82/35/a78235ab384d29b252b504f9f03cffba.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Elegant dress",
                "image_url": "https://i.pinimg.com/236x/51/b8/26/51b82639221108d853315acdee98d459.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Hoodies",
                "image_url": "https://i.pinimg.com/236x/3b/52/80/3b5280857ad7c924ef7ed1e32a1b01ef.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "High waist flared pants",
                "image_url": "https://i.pinimg.com/236x/b4/2d/0b/b42d0bb441894ecee38db423e0f978ef.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
             {
                "name": "Slim leggings",
                "image_url": "https://i.pinimg.com/236x/48/12/67/481267b9a1ecf554598383d7c06ef413.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
             {
                "name": "Leather jacket",
                "image_url": "https://i.pinimg.com/236x/bb/d9/d5/bbd9d527f153e92845967e5eaf6cbd28.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Leather jacket",
                "image_url": "https://i.pinimg.com/236x/7e/f8/51/7ef851cf4e8b9d2739e9147719bc7df7.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Suspender overalls",
                "image_url": "https://i.pinimg.com/236x/86/2a/3f/862a3f5f9d4038b2a5a9efecbbfc0362.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Denim Pants",
                "image_url": "https://i.pinimg.com/236x/cb/40/eb/cb40eb435daf9c89f82b8c788cc073cb.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Denim Shorts",
                "image_url": "https://i.pinimg.com/236x/72/3c/a4/723ca4a8c6408fe3572ab375376a2103.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Denim Pants",
                "image_url": "https://i.pinimg.com/236x/43/14/4e/43144ef2c3230817df42ab8849b993e8.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Tops",
                "image_url": "https://i.pinimg.com/236x/04/63/fc/0463fc931ae258c47c012730d1ef60a3.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Tops",
                "image_url": "https://i.pinimg.com/236x/02/5a/bb/025abb3d33c3123ee7e52a078bd5b7b8.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Baggy Trousers",
                "image_url": "https://i.pinimg.com/236x/a4/d7/03/a4d70343a279e2e3a01fd55083af4237.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Cargo pants",
                "image_url": "https://i.pinimg.com/236x/30/b9/b2/30b9b2d3725dd8186dc8983352fb0887.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Swim set",
                "image_url": "https://i.pinimg.com/236x/71/5e/e3/715ee33676ba279c1fef54eaf73615c5.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Ripped Jeans",
                "image_url": "https://i.pinimg.com/236x/03/a7/b7/03a7b7a1ee2295f967cb1c5945bb65e4.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Buttoned tops n pants",
                "image_url": "https://i.pinimg.com/236x/64/8f/30/648f3020434e651efefdaaee1604d9c0.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Slit skirt",
                "image_url": "https://i.pinimg.com/236x/c2/83/90/c283905f5f062b5139fc34322d97bb89.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Collar tops",
                "image_url": "https://i.pinimg.com/236x/ae/6f/89/ae6f89f91e3f03487eca420f18b2eedf.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Oversized t-shirt",
                "image_url": "https://i.pinimg.com/236x/db/2a/b5/db2ab5e1769322075e5ac2e9731cd71e.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "Corsetts",
                "image_url": "https://i.pinimg.com/236x/1c/a1/02/1ca1029842d76d8374ce70b4ff6ca190.jpg",
                "description": "Elegant clothes perfect fittings.",
                "price": 79.99,
                "stock": 50,
                "category_id": 4  # Women's Clothing
            },
            {
                "name": "High Heels",
                "image_url": "https://i.pinimg.com/236x/cd/0d/a1/cd0da1a480eb7c54773d22d9682478eb.jpg",
                "description": "Chic high heels suitable for formal events.",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Thick sneakers",
                "image_url": "https://i.pinimg.com/236x/cd/cd/32/cdcd3280c5ae1dd49ff949fb44f2bf43.jpg",
                "description": "Stylish shoes available in all sizes.",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Loafers",
                "image_url": "https://i.pinimg.com/236x/69/4b/91/694b91faf8ecff04aa3e4e0cf01f0f66.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Casual shoes",
                "image_url": "https://i.pinimg.com/236x/b2/00/29/b20029cc93a870d0d602b219d5443bbe.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Vans",
                "image_url": "https://i.pinimg.com/236x/5a/b4/9e/5ab49ec79e6a1d252a2c322b867ab83b.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Wedge platform",
                "image_url": "https://i.pinimg.com/236x/61/99/bc/6199bcb1ad55ce7166ef49cc7b8722d2.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Mules shoes",
                "image_url": "https://i.pinimg.com/236x/f5/a9/fc/f5a9fc1b3dccfea5bbcfd57f49104fad.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Flat sandals",
                "image_url": "https://i.pinimg.com/236x/e7/2b/70/e72b7012af982ebb2bb0f7a1fb2f10b8.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Front skate shoes",
                "image_url": "https://i.pinimg.com/236x/80/d4/9e/80d49ebc4da24018505743dab9b7ccdf.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Open shoes",
                "image_url": "https://i.pinimg.com/236x/a3/87/95/a38795e2e9a650fbf13324f3707f941a.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Valentino Heels",
                "image_url": "https://i.pinimg.com/236x/62/8d/f4/628df412d2f784b40230ce366f7442b0.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Boots",
                "image_url": "https://i.pinimg.com/236x/6b/3d/3a/6b3d3af0a028eb7976856385ff69f5dd.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Sandals",
                "image_url": "https://i.pinimg.com/236x/1a/05/5a/1a055af04a063eced6110ebda4320dc3.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Boots",
                "image_url": "https://i.pinimg.com/236x/e5/ec/e3/e5ece3de0fbbaae2fb6edf2b57fe51a4.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Flatforms",
                "image_url": "https://i.pinimg.com/236x/72/bf/99/72bf99ad8ad30985d828d3d54f8806af.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Filas",
                "image_url": "https://i.pinimg.com/236x/90/e3/0b/90e30be9a1acb7a432cb3fc4968f3af2.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "High heels",
                "image_url": "https://i.pinimg.com/236x/4e/a6/6e/4ea66e52239d6bc956b0e08ec2655ad5.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Ankle boots",
                "image_url": "https://i.pinimg.com/236x/b6/fc/52/b6fc521a2239e5196e499ec699d89a03.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Slides",
                "image_url": "https://i.pinimg.com/236x/3b/ec/7b/3bec7b9b7cb55d83a15e61045fff1296.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Chunky Loafers",
                "image_url": "https://i.pinimg.com/474x/5d/23/90/5d239075f9b26cd756d87bc47496d7e8.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Leather sneakers",
                "image_url": "https://i.pinimg.com/236x/d1/33/95/d13395ee0fc791cbc55ac08e29248696.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Converse",
                "image_url": "https://i.pinimg.com/236x/56/c9/8f/56c98fc2e2d428ef0d2e3cdb9210ef87.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Stiletto heels",
                "image_url": "https://i.pinimg.com/236x/d1/01/74/d10174be5d5f0e869ebaa839c5675bc3.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Knit sock ankle boots",
                "image_url": "https://i.pinimg.com/236x/84/88/1a/84881a965254fe495d9647b716a753ac.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Platforms",
                "image_url": "https://i.pinimg.com/236x/d3/d5/3e/d3d53e766fcf529f7d19e6ca34abe42b.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Sneaker sock",
                "image_url": "https://i.pinimg.com/236x/88/36/c4/8836c4c2a3e21f801cb5445dcd837693.jpg",
                "description": "Stylish shoes available in all sizes",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Puma shoes",
                "image_url": "https://i.pinimg.com/236x/7b/c0/d7/7bc0d752726cd8fbc33895cef939aae6.jpg",
                "description": "Chic high heels suitable for formal events.",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Boots",
                "image_url": "https://i.pinimg.com/236x/a5/da/11/a5da117adf94ff1736028fda856b628d.jpg",
                "description": "Chic high heels suitable for formal events.",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Thigh high boots",
                "image_url": "https://i.pinimg.com/236x/25/cd/cf/25cdcf6144a5f1940eb7cc0210119fe3.jpg",
                "description": "Chic high heels suitable for formal events.",
                "price": 129.99,
                "stock": 50,
                "category_id": 5  # Women's Shoes
            },
            {
                "name": "Pearl earings",
                "image_url": "https://i.pinimg.com/236x/89/c5/be/89c5be7b8b3b2e504974b6aa579982ea.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Hair clips",
                "image_url": "https://i.pinimg.com/236x/8d/f4/12/8df41263210037ae82bfaa0710a4530a.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Rings",
                "image_url": "https://i.pinimg.com/236x/27/5b/e1/275be107dd699845fba491ccbcc29f2a.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Scarf",
                "image_url": "https://i.pinimg.com/236x/f9/6d/48/f96d48cc01baead5af25c63c13eef1cc.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Bracelet ring",
                "image_url": "https://i.pinimg.com/236x/f0/62/bf/f062bfbffbbc48d2ecc8aaf8c74eaca0.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Modern earings",
                "image_url": "https://i.pinimg.com/236x/10/eb/67/10eb67dad86363466af276aea11470a3.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Waterproof earings",
                "image_url": "https://i.pinimg.com/236x/90/fc/24/90fc24423fc52e6faaa6babd2564e78a.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Watches",
                "image_url": "https://i.pinimg.com/236x/ff/7b/ad/ff7bad32c779cc8831228eee3166e04f.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Dumpling bag",
                "image_url": "https://i.pinimg.com/236x/8a/6a/70/8a6a70066b2f8e7cb86208a2dd517f82.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Headbands",
                "image_url": "https://i.pinimg.com/236x/70/ae/aa/70aeaae075f1d1fb312909cc6a097c7d.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Bracelets",
                "image_url": "https://i.pinimg.com/236x/4b/13/db/4b13db4a6b7db9916892e368690bf564.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Headband",
                "image_url": "https://i.pinimg.com/236x/f1/a4/17/f1a4179ea29296663ae35157efeccce3.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Anklet",
                "image_url": "https://i.pinimg.com/236x/cd/e6/d6/cde6d6d776e52e7d61079ab5131d6a11.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Handbag",
                "image_url": "https://i.pinimg.com/236x/32/fa/fd/32fafd657c3054ded885e376d42a8ff9.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Sunglasses",
                "image_url": "https://i.pinimg.com/236x/18/23/14/182314c5016283139b4d8a7ff254e502.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Stainless steel necklace",
                "image_url": "https://i.pinimg.com/236x/95/ee/b0/95eeb0da151a90dab4fc0d223c9f5ff3.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Polygon frames",
                "image_url": "https://i.pinimg.com/236x/11/20/00/112000c3e671ff22d7a548b2971d1e06.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Hoop earings",
                "image_url": "https://i.pinimg.com/236x/6b/be/c1/6bbec1ea9c766d2405ac8e71140a676a.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Fireflame sunglasses",
                "image_url": "https://i.pinimg.com/236x/f9/1c/a2/f91ca2c060e32851a7b144ee54a4a508.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            },
            {
                "name": "Caps",
                "image_url": "https://i.pinimg.com/236x/45/79/a7/4579a7f64ebc41dc5dda7e3cf1c2d94e.jpg",
                "description": "Classic accesories that add elegance to any outfit.",
                "price": 89.99,
                "stock": 50,
                "category_id": 6  # Women's Accessories
            }
        ]

        # Create Product objects from the predefined data
        products = [Product(name=prod["name"], image_url=prod["image_url"], description=prod["description"], 
                            price=prod["price"], stock=prod["stock"], category_id=prod["category_id"]) 
                    for prod in products_data]

        # Clear existing products and insert predefined products
        db.session.query(Product).delete()
        db.session.bulk_save_objects(products)
        db.session.commit()

        logging.info("Products seeded.")
        return products

if __name__ == "__main__":
    delete_existing_data()
    categories = seed_categories()
    seed_products(categories)
