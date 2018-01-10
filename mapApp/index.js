var express = require('express')
var open = require('open')
var fs = require('fs')
var path = require('path')
var app = express()
var exphbs = require('express-handlebars')
app.engine('handlebars', exphbs({
  defaultLayout: 'main'
}))
app.set('view engine', 'handlebars')

app.use(express.static(path.join(__dirname, '/lib')))
app.use(express.static(path.join(__dirname, '/src')))
app.use(express.static(path.join(__dirname, '/data')))
app.use(require('body-parser')())

app.get('/', function (req, res) {
  var geoCoordMap = fs.readFileSync(path.join(__dirname, '/data', 'city_location.json'))
  var seriesData = fs.readFileSync(path.join(__dirname, '/data', 'city_counter.json'))
  res.render('friendMap', {
    geoCoordMap: geoCoordMap,
    seriesData: seriesData
  })
})

app.listen(3000, function () {
  open('http://localhost:3000')
})
