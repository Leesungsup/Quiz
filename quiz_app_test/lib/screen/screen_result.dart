import 'dart:html';

import 'package:flutter/material.dart';
import 'package:quiz_app_test/model/model_quiz.dart';
class ResultScreen extends StatelessWidget{
  List<int> answer;
  List<Quiz> quizs;
  ResultScreen({this.answers, this.quizs});
  @override
  Widget build(BuildContext context){
    Size screenSize = MediaQuery.of(context).size;
    double width = screenSize.width;
    double height=screenSize.height;
    int score=0;
    for(int i=0;i<quizs.length;i++){
      if(quizs[i].answer==answer[i]){
        score+=1;
      }
    }
    return SafeArea(
      child : Scaffold(appBar: AppBar(
        title:Text('My Quiz APP Test'),
        backgroundColor: Colors.deepPurple
        ,leading:Container(),)
        ,body:Center(child:Container(decoration: BoxDecoration(borderRadius: BorderRadius.circular(20),
        border:Border.all(color:Colors.deepPurple),
        color:Colors.deepPurple,),
        width:width*0.85,
        height:height*0.5,
        child:Column(children: <Widget>[],)
        )
        )
        )
    )
  }
}