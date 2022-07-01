<template>
  <v-container fluid>
    <div class="dashboard-page">
      <v-row no-gutters class="d-flex justify-space-between mt-10 mb-6">
        <h1 class="page-title">Your Plan</h1>
        <v-menu offset-y>
        </v-menu>
      </v-row>
      <v-row>

        <v-col lg="12" sm="6" md="7" cols="12">
          <v-card class="mx-1 mb-1">
            <v-card-title class="pa-6 pb-3">
              <p>Your Performance</p>
              <v-spacer></v-spacer>
              <v-menu>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon color="textColor">mdi-dots-vertical</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                      v-for="(item, i) in mock.menu"
                      :key="i"
                      @click="() => {}"
                  >
                    <v-list-item-title>{{ item }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-card-title>
            <v-card-text class="pa-6 pt-0">
              <v-row no-gutters class="pb-5">
                <div class="mr-4">
                  <v-icon color="primary" class="ml-n2">
                    mdi-circle-medium
                  </v-icon>
                  <span class="card-light-grey">Today Calories</span>
                </div>
                <div>
                  <v-icon color="warning"> mdi-circle-medium</v-icon>
                  <span class="card-light-grey">Your Goal</span>
                </div>
              </v-row>
              <v-row no-gutters class="pb-3">
                <v-col>
                  <div class="text-h6 card-light-grey font-weight-regular">
                    Today Calories
                  </div>
                  <v-progress-linear
                      :value="value"
                      background-color="#ececec"
                      color="primary"
                  ></v-progress-linear>
                </v-col>
              </v-row>
              <v-row no-gutters class="pb-1">
                <v-col>
                  <div class="text-h6 card-light-grey font-weight-regular">
                    Your Goal
                  </div>
                  <v-progress-linear
                      :value="value2"
                      background-color="#ececec"
                      color="warning"
                  ></v-progress-linear>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>

      </v-row>
      <v-row no-gutters>
        <v-col cols="12" md="6">
          <v-card class="mx-1 mb-1">
            <v-card-title class="pa-6 pb-3">
              <p>Apex Line Chart</p>
              <v-spacer></v-spacer>
              <v-menu>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                      icon
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-icon color="textColor">mdi-dots-vertical</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                      v-for="(item, i) in menu"
                      :key="i"
                      @click="() => {}"
                  >
                    <v-list-item-title>{{ item }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-card-title>
            <v-card-text class="pa-6 pt-0">
              <v-row no-gutters>
                <v-col cols="12">
                  <ApexChart
                      type="area"
                      height='350'
                      :options="apexArea.options"
                      :series="apexArea.series"
                  ></ApexChart>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="mx-1 mb-1">
            <v-card-title class="pa-6 pb-3">
              <p>Apex Heatmap Chart</p>
              <v-spacer></v-spacer>
              <v-menu>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                      icon
                      v-bind="attrs"
                      v-on="on"
                  >
                    <v-icon color="textColor">mdi-dots-vertical</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                      v-for="(item, i) in menu"
                      :key="i"
                      @click="() => {}"
                  >
                    <v-list-item-title>{{ item }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-card-title>
            <v-card-text class="pa-6 pt-0">
              <v-row no-gutters>
                <v-col>
                  <ApexChart
                    type="donut"
                    :height=396
                    :options="apexPie.options"
                    :series="apexPie.series"
                  ></ApexChart>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col cols="12">
          <v-card class="support-requests mx-1 mb-1">
            <v-card-title class="pa-6 pb-0">
              <p>Your Past Meals</p>
              <v-spacer></v-spacer>
              <v-menu>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon color="textColor">mdi-dots-vertical</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                      v-for="(item, i) in mock.menu"
                      :key="i"
                      @click="() => {}"
                  >
                    <v-list-item-title>{{ item }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-card-title>
            <v-card-text class="pa-0">
              <v-simple-table>
                <template v-slot:default>
                  <thead class="pl-2">
                  <tr>
                    <th class="text-left pa-6">MEAL NAME</th>
                    <th class="text-left">TOTAL CALORIES</th>
                    <th class="text-left">TOTAL PROTEINS</th>
                    <th class="text-left">TOTAL FATS</th>
                    <th class="text-left">TOTAL CARBS</th>
                    <th class="text-left">STATUS</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="item in mock.table" :key="item.name">
                    <td class="pa-6">{{ item.name }}</td>
                    <td>{{ item.product }}</td>
                    <td>{{ item.price }}</td>
                    <td>{{ item.date }}</td>
                    <td>{{ item.city }}</td>
                    <td v-if="item.status === 'Sent'">
                      <v-chip link color="success" class="ma-2 ml-0">
                        Sent
                      </v-chip>
                    </td>
                    <td v-else-if="item.status === 'Pending'">
                      <v-chip link color="warning" class="ma-2 ml-0">
                        Pending
                      </v-chip>
                    </td>
                    <td v-else-if="item.status === 'Declined'">
                      <v-chip link color="secondary" class="ma-2 ml-0">
                        Declined
                      </v-chip>
                    </td>
                  </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>

  </v-container>
</template>

<script>
import mock from "./mock";
import config from "@/config";
import ApexChart from 'vue-apexcharts'


export default {
  name: "Dashboard",
  components: {
    // Trend,
    ApexChart,
  },
  data() {
    return {
      mock,
      apexLoading: false,
      value: this.getRandomInt(10, 90),
      value2: this.getRandomInt(10, 90),
      mainApexAreaSelect: "Weekly", apexArea: {
        options: {
          chart: {
            toolbar: {
              show: false,
            },
          },
          colors: [config.light.primary, config.light.success],
          dataLabels: {
            enabled: false,
          },
          xaxis: {
            type: "datetime",
            categories: [
              "2020-09-18T00:00:00",
              "2020-09-19T01:30:00",
              "2020-09-20T02:30:00",
              "2020-09-21T03:30:00",
              "2020-09-22T04:30:00",
              "2020-09-23T05:30:00",

            ],
          },
          tooltip: {
            x: {
              format: "dd/MM/yy HH:mm",
            },
          },
          legend: {
            show: false,
          },
          fill: {
            type: 'solid',
            opacity: 0.2,
            colors: [config.light.primary, config.light.success],
          },
          stroke: {
            width: 4,
            curve: 'smooth'
          },
        },
        series: [
          {
            name: "series1",
            data: [31, 40, 28, 51, 42, 109, 100],
          },
          {
            name: "series2",
            data: [11, 32, 45, 32, 34, 52, 41],
          },
        ],
      },
      apexPie: {
        options: {
          dataLabels: {
            enabled: false
          },
          colors: [config.light.error,config.light.warning, config.light.success],
          labels: ["Proteins", "Total Fats", "Carbohydrates"],
          legend: {
            position: 'bottom',
            horizontalAlign: 'center',
          }
        },
        series: this.generatePieSeries(),
      },
      apexLines: {
        options: {
          chart: {
            type: 'line',
            zoom: {
              enabled: false
            },
            toolbar: {
              show: false,
            }
          },
          colors: [config.light.primary],
          dataLabels: {
            enabled: false
          },
          stroke: {
            width: 2,
            curve: 'smooth',
            dashArray: [0, 8, 5]
          },
          markers: {
            size: 0,
            hover: {
              sizeOffset: 6
            }
          },
          xaxis: {
            categories: ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan', '06 Jan', '07 Jan', '08 Jan', '09 Jan',
              '10 Jan', '11 Jan', '12 Jan'
            ],
          },
          tooltip: {
            y: [
              {
                title: {
                  formatter: function (val) {
                    return val + " (mins)"
                  }
                }
              },
              {
                title: {
                  formatter: function (val) {
                    return val + " per session"
                  }
                }
              },
              {
                title: {
                  formatter: function (val) {
                    return val;
                  }
                }
              }
            ]
          },
          legend: {
            show: false,
          },
          grid: {
            xaxis: {
              lines: {
                show: false,
              }
            },
            yaxis: {
              lines: {
                show: false,
              },
            }
          }
        },
        series: [
          {
            name: "Session Duration",
            data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
          },
          {
            name: "Page Views",
            data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35]
          },
          {
            name: 'Total Visits',
            data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
          }
        ],
      },
      menu: [
        'Edit',
        'Copy',
        'Delete',
        'Print'
      ],
    };
  },
  methods: {
    getRandomDataForTrends() {
      const arr = [];
      for (let i = 0; i < 12; i += 1) {
        arr.push(Math.random().toFixed(1) * 10);
      }
      return arr;
    },
    generatePieSeries() {
      let series = [];

      for (let i = 0; i < 3; i++) {
        let y = Math.floor(Math.random() * (500 - 100 + 100)) + 100;
        series.push(y);
      }
      return series;
    },
    getRandomInt(min, max) {
      let rand = min - 0.5 + Math.random() * (max - min + 1);
      return Math.round(rand);
    },
  },
  mounted() {
    setTimeout(() => {
      this.apexLoading = true;
    });
  },
};
</script>

<style src="./Dashboard.scss" lang="scss"/>
