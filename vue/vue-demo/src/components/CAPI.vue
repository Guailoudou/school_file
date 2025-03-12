<template>
    <div>：{{ n }}</div>
    <button @click="addn">add</button>
    <div class=""></div>
</template>
<script setup>
import { ref } from 'vue';
const n = ref(0)
const addn = () => {
    n.value++
}
</script>
<script>
export default {
    data() {return {value: "fff"}},
    beforeCreate() {
        console.log("beforeCreate")
    },
    created(){
        console.log("created")
    }
}
</script>