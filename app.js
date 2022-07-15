//jshint esversion:6

const express = require('express');
const https = require('https');
const bodyParser = require('body-Parser');

const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/app.html');
})

app.post('/', (req, res) => {
    const location = req.body.cityName
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=9a55b5196401a859dfaa5d839cc8b493&units=metric`
    https.get(url, (response) => {
        console.log(response.statusCode);
        response.on('data', (data) => {
            const weatherData = JSON.parse(data);
            const temp = weatherData.main.temp;
            const { description, main, id, icon} = weatherData.weather[0];
            const imgURL = 'https://openweathermap.org/img/wn/' + icon + '@2x.png';

            res.write('<h1>the weather in ' + location + ' at temperature of ' + temp + 'C, will be ' + main + ' with a ' + description + '</h1>');
            res.write('<img src =' + imgURL + '>');
            res.send(); 
        });
    });
})

app.listen(3000, (req, res) => {
    console.log('server is running at port 3000!!');
})
