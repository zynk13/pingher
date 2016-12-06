$(window).load(function() {
    //Declare the speech object & set attributes
    utterance = new window.SpeechSynthesisUtterance();
    utterance.lang = 'en-US';
    utterance.volume = 1.0;
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    voices=null;
        //Speak the phrase
    window.speechSynthesis.speak(utterance);
    window.speechSynthesis.onvoiceschanged = function () {
        console.log("voice changed")
        voices = speechSynthesis.getVoices();
        utterance.voice = voices.filter(function(voice) { return voice.name == 'Google UK English Female'; })[0];
    };
    window.speechSynthesis.speak(utterance);
    PingherUtil.DetectEnter();
});


  PingherUtil={
		  startDictation : function(){
			  if (window.hasOwnProperty('webkitSpeechRecognition')) {
			      //var snd = new Audio("/static/pingherapp/assets/sounds/ahhh.wav");
			      var snd = new Audio("/static/pingherapp/assets/sounds/beep.wav");   
			      snd.play(); 
			      var recognition = new webkitSpeechRecognition();
			      recognition.continuous = false;
			      recognition.interimResults = false;
			      recognition.lang = "en-US";
			      recognition.start();
			      //if ('speechSynthesis' in window) {
         //                        voices = window.speechSynthesis.getVoices();
         //                        VoiceMsg.voice = voices.filter(function(voice) { return voice.name == 'Google UK English Female'; })[0];
         //                        console.log(VoiceMsg);       
         //                     }
			      recognition.onresult = function(e) {
    			      
                    		      document.getElementById('transcript').value= e.results[0][0].transcript;
                    		      recognition.stop();
                    		      PingherUtil.MakeAjaxCall();
                    		     
			        
			      };
			  
			      recognition.onerror = function(e) {
			        recognition.stop();
			      }
			 
			    }   
			},
		DetectEnter : function(){
          		        $("input[name='q']").bind("keypress", function(e) {
                                if (e.keyCode == 13) {
                                    PingherUtil.MakeAjaxCall();
                                }
                                });
	      },
              MakeAjaxCall : function(){
                                      var d = new Date();
                    		      var question=$("input[name='q']").val();
                    		      question=question.replace(" monetization"," demonetization");
                    		      question=question.replace("the monetization","demonetization");
                    		      var questionUI="<li class='in'><img class='avatar' alt='' src='/static/pingherapp/assets/layouts/layout/img/avatar1.jpg' /><div class='message'><span class='arrow'> </span><a href='javascript:;' class='name'> You </a><span class='datetime'> at "+d.getHours()+":"+d.getMinutes()+" </span><span class='body'>"+question+"</span></div></li>"
                       		      var parentList=$("ul.chats");
                       		      parentList.append(questionUI);
                                      data={question:question}
                                        $("input[name='q']")[0].value="";
                                        $.ajax({
                                			        	url: "askQuestion", 
                                			        	data: data,
                                			        	success: function(result){
                                            console.log(result);
                                            var d = new Date();
                                            var parentList=$("ul.chats");
                                            var urlUI="";
                                            for(var i=0;i<result.tweet_url.size;i++){
                                                console.log(result.tweet_url[i]);
                                                var urltemp="<a href='"+result.tweet_url[i]+"' target='_blank'>"+result.tweet_url[i]+"</a>&nbsp;"
                                                urlUI+=urltemp;
                                            }
                                            if(urlUI!=""){
                                                urlUI="&nbsp;URL(s) - "+urlUI
                                            }
                                            var imgUI="";
                                            for(var i=0;i<result.media_url.length;i++){
                                                console.log(result.media_url[i]);
                                                var imgTemp="<div class='tweetImgDiv'><img class='tweetImg' src='"+result.media_url[i]+"' /></div>";
                                                imgUI+=imgTemp;
                                            }
                                            
                                            //if(result.media_url!=""){
                                            //    imgUI="<div class='tweetImgDiv'><img class='tweetImg' src='"+result.media_url+"' /></div>";
                                            //}
                                            
                                            var answerUI="<li class='out'><img class='avatar' alt='' src='/static/pingherapp/assets/layouts/layout/img/avatar2.png' /><div class='message'><span class='arrow'> </span><a href='javascript:;' class='name'> Her </a><span class='datetime'> at "+d.getHours()+":"+d.getMinutes()+"</span><span class='body'>"+result.tweet_text+urlUI+"</span></div>"+imgUI+"</li>"
                                            parentList.append(answerUI);
                                            var container = $(".scroller");
                                            container.slimScroll({
                                            scrollTo: container[0].scrollHeight
                                            
                                            });
                                            if ('speechSynthesis' in window) {
                                                    utterance = new window.SpeechSynthesisUtterance();
                                                    utterance.lang = 'en-US';
                                                    utterance.volume = 1.0;
                                                    utterance.rate = 1.0;
                                                    utterance.pitch = 1.0;
                                                    utterance.voice = voices.filter(function(voice) { return voice.name == 'Google UK English Female'; })[0];
                                                        utterance.text = result.tweet_text;
                                                        window.speechSynthesis.speak(utterance);
                                            }
                                        
                                        }});    
            } 
	}