
<template>
  <div id="search-app">
    <h1 class="title">Search</h1>
      <div class="colums">
        <div class="column is-4">
          <div class="field">
            <label>Food</label>

            <div class="control">
              <input type="text" v-on:input="filteredList" v-model="input" placeholder="Search foods..."/>
              <div class="item fruit" v-for="food in foods" v-bind:key="food.id">
                <p>{{ food.name }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>

</template>
<script setup>
import {ref} from "vue";
import axios from "axios";

let foods = [];
let input = ref("");
let updateKey = 0;

async function filteredList() {
  console.log(input)
  const b = await axios
      .get('api/v1/foods/', {params:{search: input.value}})
      .then(response => {
        return response.data
      })
      .catch(error => {
        console.log(error)
      })
  console.log(b)
  updateKey++;
  foods.splice(0, foods.length)
  foods.push(...b)
}
</script>
