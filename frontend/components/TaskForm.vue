<template>
  <v-card>
    <v-card-title> {{ selectedTask === null ? "Add" : "Edit" }} Task </v-card-title>
    <v-card-text>
      <v-text-field v-model="task.name" label="Name" />
      <v-text-field v-model="task.description" label="Description" />
      <v-text-field v-model="task.duration" label="Duration" type="number" />
    </v-card-text>
    <v-card-actions>
      <v-btn @click="submitTask()" color="primary">
        {{ selectedTask === null ? "Save" : "Update" }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
const DEFAULT_FORM_STATE = {
  name: "",
  description: "",
  duration: 1
}

export default {
  props: {
    selectedTask: Object,
  },
  created() {
    this.task = this.selectedTask === null ? {...DEFAULT_FORM_STATE} : this.selectedTask
  },
  data() {
    return {
      task: {},
    }
  },
  methods: {
    async submitTask() {
      this.selectedTask === null ? this.addTask() : this.editTask()
    },
    async addTask() {
      try {
        await this.$axios.$post('/task/task', this.task)
        this.task = {...DEFAULT_FORM_STATE}
        this.$emit('submit')
      } catch (err) {
        this.$emit('displayError')
      }
    },
    async editTask() {
      try {
        await this.$axios.$patch('/task/task', this.task)
        this.task = {...DEFAULT_FORM_STATE}
        this.$emit('submit')
      } catch (err) {
        this.$emit('displayError')
      }
    },
  },
  watch: {
    selectedTask: function(newVal) {
      this.task = newVal === null ? {...DEFAULT_FORM_STATE} : newVal
    }
  },
}
</script>

<style></style>
