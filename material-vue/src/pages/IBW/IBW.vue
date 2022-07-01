<template>

  <v-container fluid class="typography-page">

    <div class="yz-widget" data-calculator-type="ideal_weight" data-language="en" data-unit-system="metric"
         data-background-color="#EEEEEE" data-text-color="#212121" data-primary-color="#536dfe"
         data-alternate-background-color="#FFFFFF" data-alternate-text-color="#FFFFFF" data-secondary-color="#FFC107">
      <span class="yz-copyright">Powered by
        <a href="https://www.yazio.com/en/ideal-weight-calculator">YAZIO</a></span>
    </div>


  </v-container>
</template>

<script>
export default {
  mounted() {

    let old = document.getElementById('calculator')
    if (old) {
      old.parentNode.removeChild(old)
      location.reload();

    }
    let Script = document.createElement("script");
    Script.setAttribute('id', 'calculator')
    Script.setAttribute("src", "https://widget.yazio.com/calculator.js" + '?cachebuster=' + new Date().getTime());
    document.head.appendChild(Script);


  }
};
</script>

<style src="./IBW.scss" scoped lang="scss"></style>
