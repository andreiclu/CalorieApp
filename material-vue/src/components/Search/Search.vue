<template>
  <form action="#">
    <label :data-state="state">
      <input type="text" v-on:input="filteredList" placeholder="Search" v-model ='input' @click="state = 'open'" @blur="state='close'"/>
      <div class="item fruit" v-for="food in foods" v-bind:key="food.id">
        <p>{{ food.name }}</p>
      </div>
      <v-icon :color="config.light.iconColor" size="28">mdi-magnify</v-icon>
    </label>
  </form>
</template>

<script>
import config from '../../config';
import axios from "axios";

export default {
  name: 'Search',
  data() {
    return {
      config,
      state: "close",
      input: '',
      foods: []
    }
  },
  methods: {
    async filteredList() {

      const b = await axios
          .get('http://127.0.0.1:8000/api/v1/foods/', {params: {search: this.input}})
          .then(response => {
            return response.data
          })
          .catch(error => {
            console.log(error)
          })
      console.log(b)
      this.foods.splice(0, this.foods.length)
      this.foods.push(...b)
    }
  }
}

</script>

<style src="./Search.scss" lang="scss"></style>


