<template>
  <v-container fluid>
    <div class="dashboard-page">
      <v-row no-gutters class="d-flex justify-space-between mt-10 mb-6">
        <h1 class="page-title">Your Plan</h1>

        <v-menu offset-y>
        </v-menu>
      </v-row>
      <v-row>
        <v-col
            cols="12"
            sm="6"
            md="4"
        >
          <v-menu
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                  v-model="date"
                  label="Select a date for other stats: "
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
                v-model="date"
                @input="getData"
            ></v-date-picker>
          </v-menu>
        </v-col>
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

              </v-row>
              <v-row no-gutters class="pb-3">
                <v-col>
                  <div class="text-h6 card-light-grey font-weight-regular">
                    Today Calories {{ calories }}/{{ goal }}
                  </div>
                  <v-progress-linear v-if="calories>goal"
                                     :value="goal/calories*100"
                                     background-color="error"
                                     color="primary"
                  ></v-progress-linear>
                  <v-progress-linear v-if="calories<=goal"
                                     :value="calories/goal*100"
                                     background-color="#ececec"
                                     color="primary"
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
              <p>Today's Macronutrients:</p>
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
import axios from "axios";


export default {
  name: "Dashboard",
  components: {
    // Trend,
    ApexChart,
  },
  data() {
    let date = new Date()
    return {
      mock,
      apexLoading: false,
      date: date.toISOString().slice(0, 10),
      calories: 0,
      goal: 2000,
      carbs: 0,
      fats: 0,
      proteins: 0,
      value2: this.getRandomInt(10, 90),
      mainApexAreaSelect: "Weekly",
      apexArea: {
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

            ],
          },
          tooltip: {
            x: {
              format: "dd/MM/yy",
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
            name: "weight",
            data: [],
          },
        ],
      },
      apexPie: {
        options: {
          dataLabels: {
            enabled: false
          },
          colors: [config.light.error, config.light.warning, config.light.success],
          labels: ["Proteins", "Total Fats", "Carbohydrates"],
          legend: {
            position: 'bottom',
            horizontalAlign: 'center',
          }
        },
        series: [0, 0, 0],
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
    getRandomInt(min, max) {
      let rand = min - 0.5 + Math.random() * (max - min + 1);
      return Math.round(rand);
    },
    getTimeSeriesData() {
      axios
          .get('http://127.0.0.1:8000/api/v1/profile-info-per-day/', {params: {date__lte: this.date, weight__gt: 0}})
          .then(response => {
            console.log(response)
            this.apexArea.series[0].data = []
            let categories = []
            for (let entry of response.data) {
              this.apexArea.series[0].data.push(entry.weight)
              categories.push(entry.date)

            }
            this.apexArea.options = {xaxis: {categories}}
          })
          .catch(error => {
            console.log(error)
          })
    },
    getData() {
      this.getTimeSeriesData()
      axios
          .get('http://127.0.0.1:8000/api/v1/profile-info-per-day/', {params: {date: this.date}})
          .then(response => {
            console.log(response)
            this.calories = response.data[0].calories
            this.proteins = response.data[0].proteins
            this.fats = response.data[0].fats
            this.carbs = response.data[0].carbs
            this.apexPie.series = [this.carbs, this.proteins, this.fats];
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  mounted() {
    setTimeout(() => {
      this.apexLoading = true;
    });
    this.getData();
  },
};
</script>

<style src="./Dashboard.scss" lang="scss"/>
