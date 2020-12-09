**Labels:**

focus

merge ready



<a href="https://github.com/zach2good"><img src="https://avatars3.githubusercontent.com/u/1389729?v=4" width="96" height="96" hspace="10"></img></a> **Issue by [zach2good](https://github.com/zach2good)**
_Thursday Jul 16, 2020 at 07:53:23_
_Originally opened as: project-topaz/topaz - Issue 853_

----

<!-- place 'x' mark between square [] brackets to affirm: -->
**_I affirm:_**
- [x] that I agree to Project Topaz's [Limited Contributor License Agreement](http://project-topaz.com/blob/release/CONTRIBUTOR_AGREEMENT.md), as written on this date
- [x] that I've _tested my code_ since the last commit in the PR, and will test after any later commits

Fixes: https://github.com/project-topaz/topaz/issues/852

Double checking where trusts ARENT allowed with:
```sql
select * from zone_settings
where not misc & 2048
```

**Notes:**
- Youtube tells me that you can't have trusts in Provenance
- I checked the inter-city airships myself, no trusts allowed

**Tested:**
- You can't summon trusts in cities
- You can summon trusts in BCNM entry zones
- If you get a level restricted or battlefield status your trusts are cleared (so, on entry)
- If you **don't** have that ROV KI you **can't summon** trusts in Shattering Stars MNK
- If you **do** have that ROV KI you **can summon** trusts in Shattering Stars MNK


----
<a href="https://github.com/ibm2431"><img src="https://avatars3.githubusercontent.com/u/13112942?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [ibm2431](https://github.com/ibm2431)**
_Monday Jul 20, 2020 at 18:45:00_

----

For reference, trusts are allowed in the following SOA and later zones:
```
INSERT INTO `zone_settings` VALUES (258,3,'127.0.0.1',54230,'Rala_Waterways',61,61,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (259,6,'127.0.0.1',54230,'Rala_Waterways_U',61,61,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (260,2,'127.0.0.1',54230,'Yahse_Hunting_Grounds',60,60,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (261,2,'127.0.0.1',54230,'Ceizak_Battlegrounds',60,60,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (262,2,'127.0.0.1',54230,'Foret_de_Hennetiel',60,60,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (263,2,'127.0.0.1',54230,'Yorcia_Weald',61,61,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (264,6,'127.0.0.1',54230,'Yorcia_Weald_U',62,62,62,62,0,0.00,0);
INSERT INTO `zone_settings` VALUES (265,2,'127.0.0.1',54230,'Morimar_Basalt_Fields',60,60,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (266,2,'127.0.0.1',54230,'Marjami_Ravine',60,60,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (267,2,'127.0.0.1',54230,'Kamihr_Drifts',72,72,57,57,0,0.00,4);
INSERT INTO `zone_settings` VALUES (268,3,'127.0.0.1',54230,'Sih_Gates',0,0,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (269,3,'127.0.0.1',54230,'Moh_Gates',0,0,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (270,3,'127.0.0.1',54230,'Cirdas_Caverns',0,0,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (271,6,'127.0.0.1',54230,'Cirdas_Caverns_U',62,62,62,62,0,0.00,0);
INSERT INTO `zone_settings` VALUES (272,3,'127.0.0.1',54230,'Dho_Gates',0,0,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (273,3,'127.0.0.1',54230,'Woh_Gates',0,0,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (274,3,'127.0.0.1',54230,'Outer_RaKaznar',73,73,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (275,0,'127.0.0.1',54230,'Outer_RaKaznar_U',62,62,62,62,0,0.00,0);
INSERT INTO `zone_settings` VALUES (276,0,'127.0.0.1',54230,'RaKaznar_Inner_Court',73,73,57,57,0,0.00,0);
INSERT INTO `zone_settings` VALUES (277,0,'127.0.0.1',54230,'RaKaznar_Turris',0,0,0,0,0,0.00,0);

INSERT INTO `zone_settings` VALUES (279,0,'127.0.0.1',54230,'Walk_of_Echoes_[P2]',0,0,0,0,0,0.00,0);

I don't know for certain about Leafallia

INSERT INTO `zone_settings` VALUES (290,0,'127.0.0.1',54230,'Desuetia_Empyreal_Paradox',0,0,0,0,0,0.00,128);
INSERT INTO `zone_settings` VALUES (291,0,'127.0.0.1',54230,'Reisenjima',79,79,79,79,0,0.00,128);
INSERT INTO `zone_settings` VALUES (292,0,'127.0.0.1',54230,'Reisenjima_Henge',0,0,0,0,0,0.00,0);
INSERT INTO `zone_settings` VALUES (293,0,'127.0.0.1',54230,'Reisenjima_Sanctorium',0,0,0,0,0,0.00,128);

INSERT INTO `zone_settings` VALUES (298,0,'127.0.0.1',54230,'Walk_of_Echoes_[P1]',186,186,186,186,0,0.00,0);
```


----
<a href="https://github.com/UynGH"><img src="https://avatars2.githubusercontent.com/u/40763842?v=4" width="48" height="48" hspace="10"></img></a> **Comment by [UynGH](https://github.com/UynGH)**
_Wednesday Jul 22, 2020 at 00:36:49_

----

Just checked for Leafallia:
![1](https://user-images.githubusercontent.com/40763842/88120828-24398780-cbc4-11ea-8395-6072bc07b328.jpg)

