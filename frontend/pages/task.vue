<template>
  <v-card>
    <v-card-title>
      Task List <v-btn icon @click="addTask()"><v-icon>mdi-plus</v-icon></v-btn>
    </v-card-title>
    <v-data-table :headers="headers" :items="tasks">
      <template v-slot:item.edit="{ item }">
        <v-btn icon @click="editTask({...item})"><v-icon>mdi-pencil</v-icon></v-btn>
      </template>
      <template v-slot:item.delete="{ item }">
        <v-btn icon @click="deleteTask(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
      </template>
      <template v-slot:body.append="{ headers }" v-if="tasks.length > 0">
        <tr class="total">
          <td v-for="(header,i) in headers" :key="i">
            <div v-if="header.value === 'name'">
                {{ 'TOTAL DURATION' }}
            </div>
            <div v-if="header.value === 'duration'">
                {{ getTotalDuration() }}
            </div>
          </td>
        </tr>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog">
      <task-form
        :selectedTask="selectedTask"
        @displayError="hasError = true"
        @submit="
          dialog = false
          getTasks()
        "
      />
    </v-dialog>
    <v-snackbar v-model="hasError" timeout="4000">
      ERROR: Please enter a valid duration (positive integer).
    </v-snackbar>
  </v-card>
</template>

<script>
import TaskForm from '../components/TaskForm.vue'
export default {
  components: { TaskForm },
  created() {
    this.getTasks()
  },
  data() {
    return {
      dialog: false,
      hasError: false,
      tasks: [],
      selectedTask: null,
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Description', value: 'description' },
        { text: 'Duration', value: 'duration' },
        { text: 'Edit', value: 'edit' },
        { text: 'Delete', value: 'delete' },
      ],
    }
  },
  methods: {
    getTotalDuration() {
      let sum = 0
      for (const task of this.tasks) {
        sum += task.duration
      }
      return sum
    },
    addTask() {
      this.dialog = true
      this.selectedTask = null
    },
    editTask(task) {
      this.dialog = true
      this.selectedTask = task
    },
    async getTasks() {
      this.tasks = await this.$axios.$get('/task/tasks')
    },
    async deleteTask(id) {
      await this.$axios.$delete('/task/task', { params: { id } })
      this.getTasks()
    },
  },
}
</script>

<style>
.total {
  background-color: lightgray;
  font-weight: bold;
}
</style>
