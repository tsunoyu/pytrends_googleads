// Create first the following four Ad Groups in Google Ads 
var adgroup_name_arr =  ["ADG_RisingKwd_Brand", "ADG_RisingKwd_nonBrand","ADG_TopKwd_Brand","ADG_TopKwd_nonBrand"];

//Get Spreadsheet Information
var ss = SpreadsheetApp.openByUrl("INSERT THE SPREADSHEET LINK HERE");


function main() {
   Logger.log(ss.getName());

  // loop for each ad group, sheets
  for (var j = 0; j < adgroup_name_arr.length; ++j){
    //Get first Sheet inforamtion
    var sheet = ss.getSheets()[j];
    //Get data only from second row except date
    var range = sheet.getRange(2, 2, 1, sheet.getLastColumn()-1).getValues();
    //Get kwd list in array
    var kwd_list = range[0];
      
    //delete null from array
    for (var k = 0; k < kwd_list.length; k++){
      if (kwd_list[k] === null || kwd_list[k] === undefined || kwd_list[k] === ""){
        kwd_list.splice(k, 1);  // delete
        if (k > 0) k--;
      }
    }

    //get adgroup info
    var adGroupIterator = AdsApp.adGroups()
    .withCondition('Name =' +adgroup_name_arr[j]) 
    .get();
    if (adGroupIterator.hasNext()) {
      var adGroup = adGroupIterator.next();
      
    Logger.log(adgroup_name_arr[j]);
    Logger.log(kwd_list);

    //create array with multi words
    var words_count = 0;
    var arr_multiwords = [];
    for(var m = 0; m < kwd_list.length; m++){
      words_count = kwd_list[m].split(' ').length;
      if (words_count > 1.0) {
         arr_multiwords.push(kwd_list[m]);
      }
    }
      Logger.log(arr_multiwords);
      
      // [Exact Match]for loop to put all kwd from array to adgroup
      for (var i = 0, len = kwd_list.length; i < len; ++i){
        adGroup.newKeywordBuilder()
          .withText("\[" +kwd_list[i]+"\]")               //get kwd from array and put in exact match
          .withCpc(1.25)                          // Optional
        //.withFinalUrl('http://www.example.com') // Optional
          .build();
      }
      
       // [Pharase Match] for loop to put all kwd from array to adgroup
      for (var i = 0, len = arr_multiwords.length; i < len; ++i){
        adGroup.newKeywordBuilder()
          .withText("\'" +arr_multiwords[i]+"\'")               //get kwd from array and put in exact match
          .withCpc(1.25)                          // Optional
        //.withFinalUrl('http://www.example.com') // Optional
          .build();
      }
    }
  }
}
