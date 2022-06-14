<template>
  <form @submit.prevent="calculate">
    <div>
      <label>height in meters</label>
      <input v-model.number="height" />
    </div>

    <div>
      <label>mass in kg</label>
      <input v-model.number="mass" />
    </div>

    <button type="submit">calculate</button>
  </form>
  <p>bmi: {{ bmi }}</p>
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
      const { height, mass } = this;
      return +height > 0 && +mass > 0;
    },
  },
  methods: {
    calculate() {
      if (!this.formValid) {
        return;
      }
      const { height, mass } = this;
      this.bmi = mass / height ** 2;
    },
  },
};
</script>