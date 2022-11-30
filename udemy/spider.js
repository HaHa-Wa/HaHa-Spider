const initCycleTLS = require('cycletls');
const express = require("express")
let cycleTLS

async function getList(url, cookie) {
    const response = await cycleTLS(url, {
            ja3: '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0',
            userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            cookies: cookie
        },
        'get');
    return response['body']
}

const app = express()

app.get('/get_mp4_list', async (req, res) => {
    ID = req.query.ID
    cookie = req.query.cookie
    const url = 'https://www.udemy.com/api-2.0/courses/' + ID + '/subscriber-curriculum-items/?page_size=200&fields[asset]=title,filename,asset_type,status,time_estimation,is_external&caching_intent=True'
    const content = await getList(url, JSON.parse(cookie))

    res.json({
        code: 200,
        message: 'success',
        data: content
    });
})

app.get('/get_mp4', async (req, res) => {
    ID = req.query.ID
    ID2 = req.query.ID2
    cookie = req.query.cookie
    const url = 'https://www.udemy.com/api-2.0/users/me/subscribed-courses/' + ID + '/lectures/' + ID2 + '/?fields[lecture]=asset,description,download_url,is_free,last_watched_second&fields[asset]=asset_type,length,media_license_token,course_is_drmed,media_sources,captions,thumbnail_sprite,slides,slide_urls,download_urls,external_url&q=0.7206636277383855'

    const content = await getList(url, JSON.parse(cookie))

    res.json({
        code: 200,
        message: 'success',
        data: content
    });
})

app.get('endSpider', (req, res) => {
    cycleTLS.exit()
    res.json({
        code: 200,
        message: 'success',
    });

})


app.listen(16060, async function () {
    cycleTLS = await initCycleTLS();

    console.log("启动服务")
})
