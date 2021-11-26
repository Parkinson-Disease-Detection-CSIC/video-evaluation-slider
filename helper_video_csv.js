function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('My Custom Menu')
    .addItem('Run My Function', 'myFunction')
    .addToUi();
}

function myFunction() {
  var sheet = SpreadsheetApp.getActiveSheet();
  sheet.appendRow(["subject", "exercise", "video_id"]);
  var folder = DriveApp.getFolderById("13QNKf1VO_TqxJZQa7SlUDFTsiSvP8PQm");
  var contents = folder.getFiles();
  var cnt = 0;
  var file;

  while (contents.hasNext()) {
    var file = contents.next();
    var file_name = file.getName().split(".")[0];
    var sub_ex = file_name.split("_");
    cnt++;
    data = [
      sub_ex[0],
      sub_ex[1],
      file.getId(),
    ];
    sheet.appendRow(data);
  };
}

