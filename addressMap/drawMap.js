// 初始化echarts示例mapChart
function initLoad() {

}

function geoCoordMap() {

}

function optionSeriesData() {

}

var mapChart = echarts.init(document.getElementById('map-wrap'))

var geoCoordMap = {
    "合肥": [117.27, 31.86],
    "武汉": [114.31, 30.52],
    "大庆": [125.03, 46.58]
};

var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

option = {
    backgroundColor: '#404a59',
    title: {
        text: '全国主要城市空气质量',
        subtext: 'data from PM25.in',
        sublink: 'http://www.pm25.in',
        x: 'center',
        textStyle: {
            color: '#fff'
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: function (params) {
            return params.name + ' : ' + params.value[2];
        }
    },
    legend: {
        orient: 'vertical',
        y: 'bottom',
        x: 'right',
        data: ['pm2.5'],
        textStyle: {
            color: '#fff'
        }
    },
    visualMap: {
        min: 0,
        max: 200,
        calculable: true,
        inRange: {
            color: ['#50a3ba', '#eac736', '#d94e5d']
        },
        textStyle: {
            color: '#fff'
        }
    },
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        itemStyle: {
            normal: {
                areaColor: '#323c48',
                borderColor: '#111'
            },
            emphasis: {
                areaColor: '#2a333d'
            }
        }
    },
    series: [{
        name: 'pm2.5',
        type: 'scatter',
        coordinateSystem: 'geo',
        data: convertData([{
                name: "合肥",
                value: 229
            },
            {
                name: "武汉",
                value: 273
            },
            {
                name: "大庆",
                value: 279
            }
        ]),
        symbolSize: 12,
        label: {
            normal: {
                show: false
            },
            emphasis: {
                show: false
            }
        },
        itemStyle: {
            emphasis: {
                borderColor: '#fff',
                borderWidth: 1
            }
        }
    }]
}
mapChart.setOption(option)