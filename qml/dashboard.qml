import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 760
    height: 500
    visible: true
    title: qsTr("App Home")

    // SET MATERIAL STYLE
    Material.theme: Material.White
    Material.accent: Material.LightBlue

    // CUSTOM PROPERTIES
    property string textUsername

    // FOOTER

    Rectangle{
        id: topBar
        height: 40
        color: Material.color(Material.Grey)
        anchors{
            left: parent.left
            right: parent.right
            top: parent.top
            margins: 10
        }
        radius: 10
    Text{
        id: textUser
        text: textUsername
        anchors.verticalCenter: parent.verticalCenter
        verticalAlignment: Text.AlignVCenter
        color: "#ffffff"
        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: 10
    }
    }


}