// var csrftoken = Cookies.get('csrftoken');
// Vue.http.headers.common['HTTP_X_CSRFTOKEN'] = csrftoken;
const app = new Vue({
    el: '#employee',

    delimiters: ["<%", "%>"],


    data: {
        name : 'Test',
        task_list: '',
        // csrf_token1: '',
        add_task: false,
        data_to_save : {
            task_name: ''
        },
        get_query : `query{
            allUser: employee(id:1){
              id
              username
              taskSet{
                id
                task
                status
              }
            }
          }`
    },

    computed: {
        
    },
    mounted() {
        this.getAllTasks()
    },
    methods: {

        getAllTasks() {

            fetch('/emp/graphql', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ query: this.get_query }),
            }).then(response => {
                return response.json()
            }).then(json => {
                this.task_list = json.data.allUser.taskSet
            })
        
        },
        csvfiledownload() {
            let csvContent = "data:text/csv;charset=utf-8,";
            csvContent += [
                Object.keys(this.task_list[0]).join(","),
                ...this.task_list.map(item => Object.values(item).join(","))
            ]
                .join("\n")
                .replace(/(^\[)|(\]$)/gm, "");

            const data = encodeURI(csvContent);
            const link = document.createElement("a");
            link.setAttribute("href", data);
            link.setAttribute("download", "export.csv");
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        },
        saveTask(){
            fetch('/emp/add_task', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ name: this.data_to_save.task_name }),
            }).then(response => {
                return response.json()
            }).then(json => {
                this.getAllTasks()
                this.add_task = false
            })
        }
    }
})