<template>
  <form @submit.prevent="calculate">
    <div>
      <label>height in meters</label>
      <input v-model.number="height"/>
      <select name='gender' id='gender'>
        <option value="female" selected="selected">Female</option>
        <option value="male" selected="male">Male</option>
      </select>
    </div>

    <div>
      <label>mass in kg</label>
      <input v-model.number="mass"/>
    </div>

    <button type="submit">calculate</button>

  </form>
  <p>bmi: {{ bmi.toFixed(2) }}</p>

<script>
export default {
  name: "IDC"
}
</script>

<style scoped>

</style>