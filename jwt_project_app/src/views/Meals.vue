import {
VueCollapsiblePanelGroup,
VueCollapsiblePanel,
} from '@dafcoe/vue-collapsible-panel'

<template>
  <h1><input v-on:input="getMeals" type="date" v-model="date"/></h1>
  <div class="control">
    <form v-if="openedMealForm">
      <label> Title
        <input v-model="newMealTitle">
      </label>
      <label> Meal time
        <input type="time" v-model="newMealTime" required>
      </label>
      <button v-on:click="addMeal">Create new meal</button>
    </form>
    <button v-else v-on:click="openedMealForm = !openedMealForm">Add meal</button>
    <form v-if="openedAddFoodForm">
      <div class="control">
        <label>Food
          <input list="foodSearch" type="text" v-on:input="filteredList" v-model="searchInput"
                 placeholder="Search foods..."/>
          <select v-model="addFoodId" id="foodSearch" class="item fruit dropdown-content" v-for="food in foods"
                    v-bind:key="food.id">
            <option :value="food.id">{{ food.name }}</option>
          </select>
        </label>
        <label>Quantity
          <input type="number" v-model="addFoodNumber" required>
        </label>

        <button v-on:click="addFoodToMeal">Add to meal</button>
      </div>
    </form>
    <vue-collapsible-panel-group>
      <div class="item meal" v-for="meal in meals" v-bind:key="meal.id">
        <vue-collapsible-panel v-on:click="getFoodsForMeal(meal.id)" :expanded="false">
          <template #title>
            <p>{{ meal.title }}</p>
            <p>{{ meal.time }}</p>
          </template>
          <template #content>
            <button v-on:click="openAddFoodForm(meal.id)">Add food</button>
            <p> Foods </p>
            <div class="item food" v-for="food in getFoodsForId(meal.id)" v-bind:key="food.id">
              <p>{{ food.food.name }}</p>
              <p>{{ food.number }}</p>
            </div>
          </template>
        </vue-collapsible-panel>

      </div>
    </vue-collapsible-panel-group>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "meals",
  data() {
    let date = new Date()
    return {
      date: date.toISOString().slice(0, 10),
      meals: [],
      foodsPerMeal: {},
      foods: [],
      searchInput: "",
      updateKey: 0,
      openedMealForm: false,
      openedAddFoodForm: false,
      newMealTime: date.toTimeString().split(' ')[0].slice(0, -3),
      newMealTitle: "",
      addToMealId: 0,
      addFoodNumber: 0,
      addFoodId: 0
    }
  },
  methods: {
    getMeals(e) {
      axios
          .get('api/v1/meals/', {params: {date: this.date}})
          .then(response => {
            console.log(response)
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
            console.log(response)
            this.meals = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    getFoodsForId(id) {
      return this.foodsPerMeal[id] || []
    }
    ,
    async filteredList() {
      const b = await axios
          .get('api/v1/foods/', {params: {search: this.searchInput}})
          .then(response => {
            return response.data
          })
          .catch(error => {
            console.log(error)
          })
      console.log(b)
      this.updateKey++;
      this.foods.splice(0, this.foods.length)
      this.foods.push(...b)
    },
    getFoodsForMeal(id, event) {
      axios
          .get('api/v1/foods-per-meal/', {params: {meal: id}})
          .then(response => {
            console.log(response)
            this.foodsPerMeal[id] = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
  ,
  beforeMount() {
    this.getMeals()
  }
  ,
}

</script>

<style scoped>

</style>