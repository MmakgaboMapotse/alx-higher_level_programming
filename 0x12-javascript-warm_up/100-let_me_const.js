#!/usr/bin/node

const fs = require('fs');

const myVarFilePath = 'path_to_your_file'; // Replace 'path_to_your_file' with the path to your file

fs.readFile(myVarFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const modifiedData = data.replace(/myVar\s*=\s*\d+/, 'myVar = 333');

    fs.writeFile(myVarFilePath, modifiedData, 'utf8', (err) => {
        if (err) {
            console.error(err);
            return;
        }

        console.log('Value of myVar modified to 333 successfully.');
    });
});

