const gm = require('gm').subClass({imageMagick: true})
const path = require('path')
const os = require('os');
const rootPath = path.resolve(__dirname, '..')
// sudo apt install graphicsmagick
// sudo apt install imagemagick-6.q16

convertAllImages = async () => {
    
    const testFolder = '../images/';
    const fs = require('fs');

    fs.readdirSync(testFolder).forEach(file => {
    convertImage(file)
    });
}

async function convertImage(filename) {
    return new Promise((resolve, reject) => {
      const inputFile = `../images/${filename}`
      const outputFile = `../images/${filename}`
      const width = 1920
      const height = 1080
      gm()
        .in(inputFile)
        .out('(')
          .out('-clone')
          .out('0')
          .out('-background', 'white')
          .out('-blur', '0x9')
          .out('-resize', `${width}x${height}^`)
        .out(')')
        .out('(')
          .out('-clone')
          .out('0')
          .out('-background', 'white')
          .out('-resize', `${width}x${height}`)
        .out(')')
        .out('-delete', '0')
        .out('-gravity', 'center')
        .out('-compose', 'over')
        .out('-composite')
        .out('-extent', `${width}x${height}`)
        .write(outputFile, (error) => {
          if (error) {
            return reject(error)
          }

          console.log(`> [making-video] Image converted: ${outputFile}`)
          resolve()
        })

    })
  }

  convertAllImages()