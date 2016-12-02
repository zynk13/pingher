  PingherUtil={
		  startDictation : function(){
			  if (window.hasOwnProperty('webkitSpeechRecognition')) {
				  
			      var recognition = new webkitSpeechRecognition();
			      recognition.continuous = false;
			      recognition.interimResults = false;
			      recognition.lang = "en-US";
			      recognition.start();
			 
			      recognition.onresult = function(e) {
			        document.getElementById('transcript').value
			                                 = e.results[0][0].transcript;
			        recognition.stop();
			        //document.getElementById('labnol').submit();
			        data={question:"This is a sample question?"}
			        $.ajax({
			        	url: "askQuestion", 
			        	data: data,
			        	success: function(result){
			            console.log(result);
			        }});
			        
			      };
			 
			      recognition.onerror = function(e) {
			        recognition.stop();
			      }
			 
			    }   
			}
	}