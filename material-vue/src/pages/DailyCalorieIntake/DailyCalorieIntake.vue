<template>
  <v-container fluid class="typography-page">
    <div class="yz-widget" data-calculator-type="daily_need" data-language="en" data-unit-system="metric"
         data-background-color="#EEEEEE" data-text-color="#212121" data-primary-color="#536dfe"
         data-alternate-background-color="#FFFFFF" data-alternate-text-color="#FFFFFF" data-secondary-color="#FFC107">
      <span class="yz-copyright">Powered by <a
          href="https://www.yazio.com/en/calorie-intake-calculator">YAZIO</a></span></div>

  </v-container>
</template>

<script>
export default {
  mounted() {
    let Script = document.createElement("script");
    Script.setAttribute("src", "https://widget.yazio.com/calculator.js");
    document.head.appendChild(Script);
  }
};
</script>

<style src="./Typography.scss" scoped lang="scss"></style>
