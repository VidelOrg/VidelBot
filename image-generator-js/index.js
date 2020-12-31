const google = require('googleapis').google;
const customSearch = google.customsearch('v1');

const googleSearchCredentials = require('./google-search.json')

downloadImage = (imagesUrl, content) => {
    const fs = require('fs');
    const axios = require('axios');

    axios({
        url: imagesUrl[0],
        responseType: 'stream',
    }).then(
        response =>
        new Promise((resolve, reject) => {
            response.data
            .pipe(fs.createWriteStream(`${content}.png`))
            .on('finish', () => resolve())
            .on('error', e => reject(e));
        })).catch(e => 
            axios({
                url: imagesUrl[1],
                responseType: 'stream',
            }).then(
                response =>
                new Promise((resolve, reject) => {
                    response.data
                    .pipe(fs.createWriteStream(`${content}.png`))
                    .on('finish', () => resolve())
                    .on('error', e => reject(e));
                })).catch(e => console.log(e))
                )
}

async function imageRobot(content) {

    const response = await customSearch.cse.list({
        auth: googleSearchCredentials.apiKey,
        cx: googleSearchCredentials.searchEngineId,
        q: content,
        searchType:"image",
        // imgSize: 'huge',
        num: 2
    })

    const imagesUrl = response.data.items.map(item => {
        return item.link
    })

    downloadImage(imagesUrl, content)
}

imageRobot("monkey")
