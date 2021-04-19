<template>
  <div class="machine-news-container">
    <div
      class="machines"
      v-for="machine in machines.machines"
      :key="machine.machine_id"
    >
      <div class="machine">
        <MachineItem :machine="machine" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { onMounted, ref } from "vue";
import stateSite from "@/modules/site";
import MachineItem from '@/components/machine_news/MachineItem'
export default {
  components: {
    MachineItem
  },
  setup() {
    const { setSite } = stateSite;
    const machines = ref([]);

    function getMachines() {
      axios.get(process.env.VUE_APP_API_URL + "machines").then((response) => {
        machines.value = response.data;
      });
    }

    onMounted(() => {
      setSite("machine_news");
    });

    return {
      machines,
      getMachines,
    };
  },
  created() {
    this.getMachines();
  },
};
</script>

<style scoped>
.machine-news-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
}
.machines {
  display: flex;
}
.machine {
  width: 13vw;
}
</style>