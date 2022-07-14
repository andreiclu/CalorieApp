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
                  label="Date: "
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
              <EditProfile title="Edit profile" @saved="getData"
                           :calorie-goal-default="calorieGoal"
                           :weight-goal-default="weightGoal"
                           :height-default="height"
                           :age-default="age"
              >
              </EditProfile>
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
                                     :label="calorieGoal/calories*100"
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
              <p>Weight stats: </p>
              <v-spacer></v-spacer>
              <InputMenuWeight @saved="getData">

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
              :description="bmiDescription"

          >
          </FactCard>

        </v-col>
        <v-col cols="12" md="3">


          <FactCard
              :title="toWeightGoal>0 ? 'Lose' : 'Gain'"
              :value="Math.abs(toWeightGoal)"
              :description="toWeightGoalDescription"
              unit="kg"
          >
          </FactCard>
        </v-col>
        <v-col cols="12" md="3">

          <FactCard
              :title="totalWeightChange>0 ? 'Gained' : 'Lost'"
              :value="Math.abs(totalWeightChange)"
              :description="totalWeightChangeDescription"
              unit="kg"

          >
          </FactCard>
        </v-col>
        <v-col cols="12" md="3">


          <FactCard
              :title="recentWeightLoss>0 ? 'Gained' : 'Lost'"
              :value="Math.abs(recentWeightLoss)"
              description="in last 2 entries"
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
import EditProfile from "@/components/InputMenu/EditProfile";

export default {
  name: "Dashboard",
  components: {
    InputMenuWeight,
    FactCard,
    ApexChart,
    EditProfile

  },
  data() {
    let date = new Date()
    return {
      mock,
      age: 20,
      apexLoading: false,
      date: date.toISOString().slice(0, 10),
      calories: 0,
      calorieGoal: 0,
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
          {
            name: "BMI",
            data: []
          }
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
      totalWeightChange: 0,
      recentWeightLoss: 0,
      height: 180

    };
  },
  computed: {
    totalWeightChangeDescription() {
      return `From start until ${this.date}`
    },
    toWeightGoalDescription() {
      return `to weight goal of ${this.weightGoal} kg`
    },
    bmiDescription() {
      if (this.bmi < 18.5) {
        return "Underweight 😒"
      } else if (this.bmi >= 18.5 && this.bmi <= 24.9) {
        return "Normal Weight 😍"
      } else if (this.bmi >= 25 && this.bmi <= 29.9) {
        return "Overweight 😮"
      } else {
        return "Obese 😱"
      }

    },

  },
  methods: {
    getTimeSeriesData() {
      axios
          .get('api/v1/profile-info-per-day/', {params: {date__lte: this.date, weight__gt: 0}})
          .then(response => {
            let categories = []
            let weights = []
            let heights = []
            let bmis = []
            for (let entry of response.data) {
              weights.push(entry.weight)
              heights.push(entry.height)
              categories.push(entry.date)
              bmis.push(Number((entry.weight / Math.pow(((entry.height || this.height || 180) / 100), 2)).toFixed(1)))
            }
            this.apexArea.series[0].data = weights
            this.apexArea.series[1].data = bmis
            this.apexArea.options = {xaxis: {categories}}
            if (weights.length >= 2) {
              this.recentWeightLoss = weights[0] - weights[1]
              this.totalWeightChange = weights[0] - weights.at(-1)
            }
            if (weights.length > 0) {
              this.bmi = Number((weights[0] / Math.pow(((heights[0] || this.height || 180) / 100), 2)).toFixed(1))
            }


          })
          .catch(error => {
            console.log(error)
          })
    },
    getProfileData() {
      axios
          .get('api/v1/profiles/', {params: {date: this.date}})
          .then(response => {
            this.weightGoal = response.data.goal_weight || 0
            this.toWeightGoal = response.data.weight - response.data.goal_weight
            this.calorieGoal = response.data.calorie_goal || 0
            this.height = response.data.height
            this.age = response.data.age
          })
          .catch(error => {
            console.log(error)
          })
    },
    getDayData() {
      axios
          .get('api/v1/profile-info-per-day/', {params: {date: this.date}})
          .then(response => {
            this.calories = response.data[0].calories
            this.proteins = response.data[0].proteins
            this.fats = response.data[0].fats
            this.carbs = response.data[0].carbs
            this.apexPie.series = [Number(this.carbs.toFixed(1)),
              Number(this.proteins.toFixed(1)), Number(this.fats.toFixed(1))];
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
