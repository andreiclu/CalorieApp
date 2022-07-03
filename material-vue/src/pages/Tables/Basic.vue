<template>
  <v-container fluid>
    <div class="tables-basic">
      <h1 class="page-title mt-10 mb-6">Food & Meals</h1>
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
            @input="getMeals"
        ></v-date-picker>
      </v-menu>
      <v-dialog v-model="showFoodsPerMeal">

        <v-col cols=12>
          <v-card class="mb-1">
            <v-card-title class="pa-5 pb-3">
              <p>Meal List:</p>
              <v-spacer></v-spacer>
              <AddFoodToMeal :meal-id="displayedMeal.id" title="Add food" @saved="getMeals"
              >
              </AddFoodToMeal>
            </v-card-title>
            <v-simple-table>
              <template v-slot:default>
                <thead>
                <tr>
                  <th class="text-left pa-6">NAME</th>
                  <th class="text-left">QUANTITY</th>
                  <th class="text-left">CALORIES</th>
                  <th class="text-left">PROTEINS</th>
                  <th class="text-left">CARBS</th>
                  <th class="text-left">FATS</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="food in displayedFoods" v-bind:key="food.id">
                  <td class="pa-6">{{ food.food.name }}</td>
                  <td>{{ food.number }}</td>
                  <td>{{ food.food.calories }}</td>
                  <td>{{ food.food.protein }}</td>
                  <td>{{ food.food.carbohydrate }}</td>
                  <td>{{ food.food.total_fats }}</td>
                </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-card>
        </v-col>
      </v-dialog>

      <v-row>

        <v-col cols=12>
          <v-card class="mb-1">
            <v-card-title class="pa-5 pb-3">
              <p>Meal List:</p>
              <v-spacer></v-spacer>
              <NewMeal title="Add new meal" @saved="getMeals"
              >
              </NewMeal>
            </v-card-title>
            <v-simple-table>
              <template v-slot:default>
                <thead>
                <tr>
                  <th class="text-left pa-6">NAME</th>
                  <th class="text-left">TIME</th>
                  <th class="text-left">CALORIES</th>
                  <th class="text-left">PROTEINS</th>
                  <th class="text-left">CARBS</th>
                  <th class="text-left">FATS</th>
                </tr>
                </thead>
                <tbody>
                <tr @click="showDialog(meal)" v-for="meal in meals" v-bind:key="meal.id">
                  <td class="pa-6">{{ meal.title }}</td>
                  <td class="pa-6">{{ meal.time }}</td>
                  <td>{{ meal.calories }}</td>
                  <td>{{ meal.proteins }}</td>
                  <td>{{ meal.carbs }}</td>
                  <td>{{ meal.fats }}</td>
                </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import mock from './mock'
import axios from "axios";
import NewMeal from "@/components/InputMenu/NewMeal";
import AddFoodToMeal from "@/components/InputMenu/AddFoodToMeal";
export default {
  name: 'Tables',
  components: {
    NewMeal,
    AddFoodToMeal

  },
  data() {
    let date = new Date()
    return {
      mock,
      date: date.toISOString().slice(0, 10),
      meals: [],
      foodsPerMeal: {},
      foods: [],
      searchInput: "",
      updateKey: 0,
      openedMealForm: false,
      openedAddFoodForm: false,

      addToMealId: 0,
      addFoodNumber: 0,
      addFoodId: 0,
      currentDialogItem: null,
      showFoodsPerMeal: false,
      displayedFoods: [],
      displayedMeal: {}
    }
  },
  methods: {
    showDialog(meal) {
      this.showFoodsPerMeal = true;
      this.currentDialogItem = meal;
      axios
          .get('api/v1/foods-per-meal/', {params: {meal: meal.id}})
          .then(response => {
            this.displayedFoods = response.data
            this.displayedMeal = meal
            console.log(this.displayedFoods)
          })
          .catch(error => {
            console.log(error)
          })
    },
    getMeals() {
      axios
          .get('api/v1/meals/', {params: {date: this.date}})
          .then(response => {
            this.meals = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    addFoodToMeal() {
      axios
          .post('api/v1/foods-per-meal/', {
            number: this.addFoodNumber,
            meal: this.addToMealId, food: this.addFoodId
          })
          .then(response => {
            console.log(response)
            this.meals = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    openAddFoodForm(mealId) {
      this.openedAddFoodForm = !this.openedAddFoodForm
      this.addToMealId = mealId
    },
    addMeal() {
      axios
          .post('api/v1/meals/', {date: this.date, time: this.newMealTime, title: this.newMealTitle})
          .then(response => {
            this.meals = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    async filteredList() {
      const b = await axios
          .get('api/v1/foods/', {params: {search: this.searchInput}})
          .then(response => {
            return response.data
          })
          .catch(error => {
            console.log(error)
          })
      this.updateKey++;
      this.foods.splice(0, this.foods.length)
      this.foods.push(...b)
    },
  }
  ,
  beforeMount() {
    this.getMeals()
  }
  ,
}

</script>

<style src="./Basic.scss" lang="scss"></style>
