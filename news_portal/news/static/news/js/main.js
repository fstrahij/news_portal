new Vue({
   el: '#starting',
   delimiters: ['${','}'],
   data: {
	   news: [],
	   message: null
 	},
 	mounted: function() {
 		this.getItems();		 		
	},
	methods: {
		getItems: function() {
		  axios.get('/api/items/')
		      .then((response) => {
		        this.news = response.data.results;	
		      })
		      .catch((err) => {
		       console.log(err);
		      })
		}
	}
});