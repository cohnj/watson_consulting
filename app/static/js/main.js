$(document).ready(function(){
	$("#questionWrapper").hide();
	$("#QAWrapper").hide();
});


function node(key, value, question){
	this.key = key;
	this.value = value;
	this.question = question;
	this.left = null;
	this.right = null;
}


var root = new node('root','ACA', 'Federal or State run plan?');
var federal = new node('fed','Federal', 'Are you a person or representing a business?');
var state = new node('il','State', 'Are you looking for personal insurance or through a business?');
var fedPeople = new node('ppl','People', null);
var fedBus = new node('bus','Business', 'Are you an employee or an employer?');
var fedEmployee = new node('ee','Employee', null);
var fedEmployer = new node('er','Employer', null);
var statePeople = new node('ppl','People', null);
var stateBus = new node('bus','Business', 'Are you an employee or an employer?');
var stateEmployee = new node('ee','Employee', null);
var stateEmployer = new node('er','Employer', null);

root.left = federal;
root.right = state;
federal.left = fedPeople;
federal.right = fedBus;
fedBus.left = fedEmployee;
fedBus.right = fedEmployer;
state.left = statePeople;
state.right = stateBus;
stateBus.left = stateEmployee;
stateBus.right = stateEmployer;

var current = root;
var metaTagString = "aca";
$(".decisionTreeAnswer").click(function(){
	if($(this).attr("id") == current.left.key){
		current = current.left;
	} else {
		current = current.right;
	}
	
	if(current.left == null || current.right == null){
		$("#questionWrapper").show();
		$("#QAWrapper").show();
		$("#decisionForm").hide();
	} else {
		$("#decisionTreeQuestion").text(current.question);
		$($("#decisionForm").find('button')[0]).attr("id",current.left.key).text(current.left.value);
		$($("#decisionForm").find('button')[1]).attr("id",current.right.key).text(current.right.value);
	}
	
	metaTagString = metaTagString + "_" + current.key;
	console.log(metaTagString);
});

// $("#questionSubmit").click(function(){
// 	$.post($SCRIPT_ROOT + "/question", $("#watsonQuestion").val(), function(data){
// 		alert(data);
// 	});

$("#questionSubmit").click(function(){
	$.getJSON($SCRIPT_ROOT + "/question", {
        watsonQuestion : $("#watsonQuestion").val()}, 
        function(data){
			alert(data.result);
	});
});