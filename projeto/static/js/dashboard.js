!function(r) {
    "use strict";
    class e {
        constructor() {
            this.$body = r("body"),
                this.charts = [];
        }
        initCharts() {
            window.Apex = {
                chart: {
                    parentHeightOffset: 0,
                    toolbar: {
                        show: !1
                    }
                },
                grid: {
                    padding: {
                        left: 0,
                        right: 0
                    }
                },
                colors: ["#3e60d5", "#47ad77", "#fa5c7c", "#ffbc00"]
            };
            var e = ["#3e60d5", "#47ad77", "#fa5c7c", "#ffbc00"], t = r("#revenue-chart").data("colors"), a = {
                series: [{
                    name: "Revenue",
                    data: [440, 505, 414, 526, 227, 413, 201]
                }, {
                    name: "Sales",
                    data: [320, 258, 368, 458, 201, 365, 389]
                }, {
                    name: "Profit",
                    data: [320, 458, 369, 520, 180, 369, 160]
                }],
                chart: {
                    height: 377,
                    type: "bar"
                },
                plotOptions: {
                    bar: {
                        columnWidth: "60%"
                    }
                },
                stroke: {
                    show: !0,
                    width: 2,
                    colors: ["transparent"]
                },
                dataLabels: {
                    enabled: !1
                },
                colors: e = t ? t.split(",") : e,
                xaxis: {
                    categories: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                },
                yaxis: {
                    title: {
                        text: "$ (thousands)"
                    }
                },
                legend: {
                    offsetY: 7
                },
                grid: {
                    padding: {
                        bottom: 20
                    }
                },
                fill: {
                    opacity: 1
                },
                tooltip: {
                    y: {
                        formatter: function (e) {
                            return "$ " + e + " thousands";
                        }
                    }
                }
            }, e = (new ApexCharts(document.querySelector("#revenue-chart"), a).render(),
                ["#3e60d5", "#47ad77", "#fa5c7c", "#ffbc00"]), a = {
                    series: [{
                        name: "Mobile",
                        data: [25, 15, 25, 36, 32, 42, 45]
                    }, {
                        name: "Desktop",
                        data: [20, 10, 20, 31, 27, 37, 40]
                    }],
                    chart: {
                        height: 250,
                        type: "line",
                        toolbar: {
                            show: !1
                        }
                    },
                    colors: e = (t = r("#yearly-sales-chart").data("colors")) ? t.split(",") : e,
                    stroke: {
                        curve: "smooth",
                        width: [3, 3]
                    },
                    markers: {
                        size: 3
                    },
                    xaxis: {
                        categories: ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
                    },
                    legend: {
                        show: !1
                    }
                }, a = (new ApexCharts(document.querySelector("#yearly-sales-chart"), a).render(),
                    Apex.grid = {
                        padding: {
                            right: 0,
                            left: 0
                        }
                    },
                {
                    series: [44, 55, 13, 43],
                    chart: {
                        width: 80,
                        type: "pie"
                    },
                    legend: {
                        show: !(Apex.dataLabels = {
                            enabled: !1
                        })
                    },
                    colors: ["#1a2942", "#f13c6e", "#3bc0c3", "#d1d7d973"],
                    labels: ["Team A", "Team B", "Team C", "Team D"]
                });
            new ApexCharts(document.querySelector("#us-share-chart"), a).render();
        }
        init() {
            this.initCharts();
        }
    }
    r.Dashboard = new e,
    r.Dashboard.Constructor = e
}(window.jQuery),
function(t) {
    "use strict";
    t(document).ready(function(e) {
        t.Dashboard.init()
    })
}(window.jQuery);
