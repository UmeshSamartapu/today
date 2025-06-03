const { MongoClient } = require('mongodb');

// MongoDB connection URL and Database Name
const url = 'mongodb://localhost:27017';
const dbName = 'foodDeliveryDB';

async function run() {
  const client = new MongoClient(url);

  try {
    // Connect to MongoDB
    await client.connect();
    console.log("Connected to MongoDB!");

    // Select database and collection
    const db = client.db(dbName);
    const collection = db.collection('orders');

    // 1. Insert a document
    const newOrder = { customer: "S.RAJENDER", food: "Pizza", price: 200 };
    await collection.insertOne(newOrder);
    console.log("Order inserted successfully!");

    // 2. Read documents
    const orders = await collection.find().toArray();
    console.log("All Orders:", orders);

    // 3. Update a document
    await collection.updateOne(
      { customer: "S.RAJENDER" },
      { $set: { food: "Burger", price: 150 } }
    );
    console.log("Order updated successfully!");

    // 4. Delete a document (optional)
    // await collection.deleteOne({ customer: "S.RAJENDER" });
    // console.log("Order deleted successfully!");

  } catch (err) {
    console.error("Error:", err);
  } finally {
    // Always close the database connection
    await client.close();
    console.log("Connection closed.");
  }
}

// Run the function
run();
