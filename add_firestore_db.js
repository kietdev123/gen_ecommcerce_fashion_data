const { initializeApp } = require('firebase/app');
const fs = require("fs");
const {
    getFirestore,
    collection,
    doc,
    addDoc,
    getDoc,
    getDocs,
    updateDoc,
    deleteDoc,
  } = require('firebase/firestore');
const firebase = initializeApp({
    apiKey: process.env.apiKey,
    authDomain:  process.env.authDomain,
    projectId:  process.env.projectId,
    storageBucket:  process.env.storageBucket,
    messagingSenderId:  process.env.messagingSenderId,
    appId:  process.env.appId,
});

const db = getFirestore(firebase);

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const brands = [
    "adidas",
    "adidas Originals",
    "Blend",
    "Boutique Moschino",
    "Champion",
    "Diesel",
    "Jack & Jones",
    "Naf Naf",
    "Red Valentino",
];

const sizes = [
    "S", "M", "L"
];

async function seedDataBrand(){
    try {
        await addDoc(collection(db, 'brand'), {'names' : brands} );
        console.log('Done added brand');
    } catch (e){
        console.log(e);
    }

}

async function seedDataType(){
    fs.readFile("./type.json", "utf8", async (error, data) => {
        if (error) {
          console.log(error);
          return;
        }
        let value = JSON.parse(data)
        await addDoc(collection(db, 'product_type'), value);
        console.log('Done added product type');
    })
}

async function seedDataProduct(){
    try {
        let products = await fs.readFileSync("./products.json", 'utf8');
        products = JSON.parse(products)['data'];
        
        let query = [];

        for (let i in products){
           
            let value = products[i];
            
            value.price = getRandomInt(100000, 1000000);
            value.saleNumber = getRandomInt(0, 100);
            value.star = getRandomInt(0, 5);
  
            let sizeIndex =  getRandomInt(0, 2);

            value.size = sizes[sizeIndex];
            
            let brandIndex =  getRandomInt(0, 8);
            value.brand = brands[brandIndex];
      
            // await addDoc(collection(db, 'products'), value );
            query.push(addDoc(collection(db, 'products'), value ))
        }
        await Promise.all(query);
        console.log('Done added product');
    } catch (e){
        console.log(e);
    }  
}


async function checkProduct(){
    try {
        const products = await getDocs(collection(db, 'products'));

        let productDatas = [];

        products.forEach((doc) => {
            
            if (doc.data().imgUrls.length < 3){
                console.log(doc.data().id)
            }
          });
    } catch (e){
        console.log(e);
    }  
}
async function main(){
    // await seedDataBrand();

    console.time('seedDataType')
    await seedDataType();
    console.timeEnd('seedDataType')

    // console.time('seedDataProduct')
    // await seedDataProduct();
    // console.timeEnd('seedDataProduct')

    // console.time('checkProduct')
    // checkProduct()
    // console.timeEnd('checkProduct')
}

main();
