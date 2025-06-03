const fs = require('fs');

const fileName = 'example.txt';
const fileContent = 'Hello, this is a sample file created using Node.js!';

// 1. Write to a file
fs.writeFile(fileName, fileContent, (err) => {
  if (err) {
    console.error('Error writing file:', err);
    return;
  }
  console.log('File created and data written successfully.');

  // 2. Read from the file
  fs.readFile(fileName, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }
    console.log('File content:', data);

    // 3. Append data to the file
    fs.appendFile(fileName, '\nAppended text!', (err) => {
      if (err) {
        console.error('Error appending file:', err);
        return;
      }
      console.log('Data appended successfully.');

      // 4. Rename the file
      const newFileName = 'updated_example.txt';
      fs.rename(fileName, newFileName, (err) => {
        if (err) {
          console.error('Error renaming file:', err);
          return;
        }
        console.log('File renamed successfully.');

        // 5. Delete the file
        fs.unlink(newFileName, (err) => {
          if (err) {
            console.error('Error deleting file:', err);
            return;
          }
          console.log('File deleted successfully.');
        });
      });
    });
  });
});
