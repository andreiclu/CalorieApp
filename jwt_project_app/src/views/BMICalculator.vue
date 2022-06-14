<template>
  <form @submit.prevent="calculate">
    <div>
      <label>height in meters</label>
      <input v-model.number="height"/>
    </div>

    <div>
      <label>mass in kg</label>
      <input v-model.number="mass"/>
    </div>

    <button type="submit">calculate</button>

  </form>
  <p>bmi: {{ bmi.toFixed(2) }}</p>
  <table style="border:1px solid black;margin-left:auto;margin-right:auto;">
    <tbody>
    <tr>
      <td>Category</td>
      <td>BMI range - kg/m<sup>2</sup></td>
    </tr>
    <tr>
      <td>Severe Thinness</td>
      <td>&lt; 16</td>
    </tr>
    <tr>
      <td>Moderate Thinness</td>
      <td>16 - 17</td>
    </tr>
    <tr>
      <td>Mild Thinness</td>
      <td>17 - 18.5</td>
    </tr>

    <tr>
      <td>Normal</td>
      <td>18.5 - 25</td>
    </tr>
    <tr>
      <td>Overweight</td>
      <td>25 - 30</td>
    </tr>
    <tr>
      <td>Obese Class I</td>
      <td>30 - 35</td>
    </tr>
    <tr>
      <td>Obese Class II</td>
      <td>35 - 40</td>
    </tr>
    <tr>
      <td>Obese Class III</td>
      <td>&gt; 40</td>
    </tr>
    </tbody>
  </table>


</template>

<script>
export default {
  name: "App",
  data() {
    return {
      height: 0,
      mass: 0,
      bmi: 0,
    };
  },
  computed: {
    formValid() {
      const {height, mass} = this;
      return +height > 0 && +mass > 0;
    },
  },
  methods: {
    calculate() {
      if (!this.formValid) {
        return;
      }
      const {height, mass} = this;
      this.bmi = mass / height ** 2;
    },
  },
};
</script>
