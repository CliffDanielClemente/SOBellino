# SOBellino

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
## Introduction

SOBellino is the perfect learning buddy for German-speaking train drivers, that are employed by SOB Südostbahn, to keep practicing their Italian skills to be able to communicate with Italian-speaking dispatchers in Ticino.

## Features

The educator can enter learning contents in a WebApp on metaphacts that is directly connected to the Knowledge Graph. In that WebApp the educator can perform CRUD commands to the data in the knowledge graph.

The learner, which is the train driver in this case, will be able to learn content from the VoiceFlow bot "SOBellino". Besides multiple choice or true/false-questions, the driver can also write a text or speak to the bot in order to learn and repeat the content that he had learned.

In order for VoiceFlow to get the data from the knowledge graph in metaphacts, an API server was made in Python. For each lesson, VoiceFlow will create an API request to the server to fetch data from the knowledge graph. VoiceFlow can only perform Read-commands / GET-requests as there is no need for manipulation to the knowledge graph.

## Prerequisites

- Git: https://github.com/CliffDanielClemente/SOBellino.git

- VoiceFlow: https://creator.voiceflow.com/workspace/accept-invite?inviteToken=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..fUX2Sck2DM_XoU0s.uThStOxqIq7_I4OsvnK4TcGwtkyWWTNLeI80S9E8d1xECMeya29qCai_RuLy22Uz9PiIz95t9MLLNKfcPl0NaPalnTpFUcR1b0YmjFop6sKmuH87ci0.mIJ6JY7Pi6Gn2sDFo3Hrfw

- Metaphacts: ZIP-File in Teams submission or git repository



