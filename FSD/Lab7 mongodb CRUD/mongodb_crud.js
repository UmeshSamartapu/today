const { MongoClient } = require('mongodb');

const url = 'mongodb://localhost:27017';
const dbName = 'companyDB';

async function runCRUD() {
  const client = new MongoClient(url);

  try {
    await client.connect();
    console.log("Connected to MongoDB!");

    const db = client.db(dbName);
    const employees = db.collection('employees');

    // 1. CREATE
    const employeeData = [
      { name: "Alice", position: "Developer", salary: 50000 },
      { name: "Bob", position: "Manager", salary: 70000 },
      { name: "Charlie", position: "Designer", salary: 60000 }
    ];
    await employees.insertMany(employeeData);
    console.log("Employees inserted successfully!");

    // 2. READ
    const allEmployees = await employees.find().toArray();
    console.log("All Employees:", allEmployees);

    // 3. UPDATE
    await employees.updateOne({ name: "Alice" }, { $set: { salary: 55000 } });
    console.log("Alice's salary updated!");

    // 4. DELETE
    await employees.deleteOne({ name: "Charlie" });
    console.log("Charlie deleted from the database.");

  } catch (err) {
    console.error("Error:", err);
  } finally {
    await client.close();
    console.log("Connection closed.");
  }
}

runCRUD();
