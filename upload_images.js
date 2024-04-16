const fs = require("fs");
var cloudinary = require('cloudinary').v2;

cloudinary.config({ 
    cloud_name: process.env.cloud_name, 
    api_key: process.env.api_key, 
    api_secret: process.env.api_secret,
  });

  let imageUrls = [];
fs.readFile("./products.json", "utf8", async (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(data)['data'][0]);

  let products = JSON.parse(data)['data'];

  for (let i  in products) {
    let result = await cloudinary.uploader
    .upload(`./data/images/${products[i].id}.jpg`, { folder: "e_commerce_fashion" })
        imageUrls.push({
            productId: products[i].id,
            url: result.url,
        })
        console.log(`Uploaded image ${i}`);
    }
    await fs.writeFileSync("./product_images.json",JSON.stringify({
        'data' : imageUrls
    }), 'utf8');
}

);



