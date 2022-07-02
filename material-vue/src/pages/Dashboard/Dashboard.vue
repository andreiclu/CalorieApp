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
                    Today Calories {{ calories }}/{{ calorieGoal }}
                  </div>
                  <v-progress-linear v-if="calories>calorieGoal"
                                     :value="calorieGoal/calories*100"
                                     background-color="error"
                                     color="primary"
                  ></v-progress-linear>
                  <v-progress-linear v-if="calories<=calorieGoal"
                                     :value="calories/calorieGoal*100"
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
              <InputMenuWeight @saved="getTimeSeriesData">

              </InputMenuWeight>
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
              <p style="padding: 5px">Today's Macronutrients:</p>
              <v-spacer></v-spacer>
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
      <v-row no-gutters

      >
        <v-col cols="12" md="3">

          <FactCard
              title="BMI"
              :value="bmi"
              description="You're fat"

          >

          </FactCard>
        </v-col>
        <v-col cols="12" md="3">


          <FactCard
              :value="toWeightGoal"
              :description="toWeightGoalDescription"
              unit="kg"
          >
            <v-card-title>
              <InputMenuWeightGoal :title="toWeightGoalTitle" @saved="getTimeSeriesData">

              </InputMenuWeightGoal>
            </v-card-title>
          </FactCard>
        </v-col>
        <v-col cols="12" md="3">

          <FactCard
              title="Total weight change"
              :value="totalWeightChange"
              description="From start till now"
              unit="kg"

          >
          </FactCard>
        </v-col>
        <v-col cols="12" md="3">


          <FactCard
              title="Recent weight loss"
              :value="recentWeightLoss"
              description="=last 2 entries"
              unit="kg"

          >

          </FactCard>
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
import FactCard from "@/components/FactCard/FactCard";
import InputMenuWeight from "@/components/InputMenu/InputMenuWeight";
import InputMenuWeightGoal from "@/components/InputMenu/InputMenuWeightGoal";

export default {
  name: "Dashboard",
  components: {
    InputMenuWeightGoal,
    InputMenuWeight,
    FactCard,
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
      calorieGoal: 2000,
      carbs: 0,
      fats: 0,
      proteins: 0,
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
            categories: [],
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
      bmi: 0,
      toWeightGoal: 0,
      weightGoal: 0,
      toWeightGoalDescription: '!',
      totalWeightChange: +20,
      recentWeightLoss: -2,
      toWeightGoalTitle: ""

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
    getProfileData() {
       axios
          .get('http://127.0.0.1:8000/api/v1/profiles/', {params: {date: this.date}})
          .then(response => {
            console.log(response)
            this.weightGoal = response.data.goal_weight || 0
            this.toWeightGoalTitle = response.data.weight> response.data.goal_weight ? "Lose" : "Gain"
            this.toWeightGoal = Math.abs(response.data.weight - response.data.goal_weight)
            this.toWeightGoalDescription = 'to weight goal of ' + this.weightGoal + ' kg'
            this.calorieGoal = response.data.calorie_goal || 0
          })
          .catch(error => {
            console.log(error)
          })
    },
    getDayData() {
      axios
          .get('http://127.0.0.1:8000/api/v1/profile-info-per-day/', {params: {date: this.date}})
          .then(response => {
            this.calories = response.data[0].calories
            this.proteins = response.data[0].proteins
            this.fats = response.data[0].fats
            this.carbs = response.data[0].carbs
            this.apexPie.series = [this.carbs, this.proteins, this.fats];
          })
          .catch(error => {
            console.log(error)
          })
    },
    getData() {
      this.getTimeSeriesData()
      this.getProfileData()
      this.getDayData()
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
