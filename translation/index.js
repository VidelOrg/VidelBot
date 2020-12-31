const fs = require('fs')
const { translate } = require("google-translate-api-browser");

translateText = () => {
    const language = process.argv[2]
    const data = readText();
    translate(data, { to: language })
    .then(res => {
      console.log(res.text)
      writeText(res.text)
    })
    .catch(err => {
      console.error(err);
    });

}

writeText = (data) => {
    fs.writeFileSync("text-out.txt", data); 
}

readText = () => {
    const filename = "text-in.txt";
    var data = fs.readFileSync(filename, 'utf8');
    return data;
}

translateText()