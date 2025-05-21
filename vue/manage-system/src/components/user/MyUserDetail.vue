<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({
id: String })
const router = useRouter() 
const goBack = () => {
router.back() }

  </script>
 <template>
    <button @click="goBack">后退</button>
    <h4>用户{{ id }}的详情页面</h4>
   </template>
 <style scoped>
 button{
  background-color: #409eff;
  color: #fff;
 }
</style>
