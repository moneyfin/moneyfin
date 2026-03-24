# moneyfin Data & Privacy
## Overview
moneyfin diagnostic data is completely optional for users and is off by default in v0.86 and beyond. Our team believes in transparency and trust. As moneyfin is open source, all of our diagnostic data events are in the codebase.

Additionally, this document aims to list each diagnostic data event individually and describe their purpose clearly.

For more information, please read the [Microsoft privacy statement](https://privacy.microsoft.com/privacystatement). 

## What does moneyfin collect?

1. **Usage**: Understanding usage and frequency rates for utilities and settings helps us make decisions on where to focus our time and energy. This data also helps us better understand what and how to move well-loved features directly into Windows!
2. **Stability**: Monitoring bugs and system crashes, as well as analyzing GitHub issue reports, assists us in prioritizing the most urgent issues.
3. **Performance**: Assessing the performance of moneyfin features to load and execute gives us an understanding of what surfaces are causing slowdowns. This supports our commitment to providing you with tools that are both speedy and effective.

### Success Story: Fixing FancyZones Bugs with Your Help
FancyZones had numerous bug reports related to virtual desktop interactions. Initially, these were considered lower priority, since the assumption was that virtual desktops were not widely used, so we chose to focus on more urgent issues. However, the volume of bug reports suggested otherwise, prompting us to add additional diagnostics to see virtual desktop usage with FancyZones. We discovered that virtual desktop usage was much higher among FancyZones users. This new understanding led us to prioritize this class of bugs and get them fixed.
 
## Transparency and Public Sharing
As much as possible, we aim to share the results of diagnostic data publicly.

We hope this document provides clarity on why and how we collect diagnostic data to improve moneyfin for our users. If you have any questions or concerns, please feel free to reach out to us.

Thank you for using moneyfin!

## List of Diagnostic Data Events
_**Note:** We're in the process of updating this section with more events and their descriptions. We aim to keep this list current by adding any new diagnostic data events as they become available._

_If you want to find diagnostic data events in the source code, these two links will be good starting points based on the source code's langauge._
- [C# events](https://github.com/search?q=repo%3Amicrosoft/moneyfin%20EventBase&type=code)
- [C++ events](https://github.com/search?q=repo%3Amicrosoft%2Fmoneyfin+ProjectTelemetryPrivacyDataTag&type=code)

### General
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.DebugEvent</td>
    <td>Logs debugging information for diagnostics and troubleshooting.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.GeneralSettingsChanged</td>
    <td>Logs changes made to general settings within moneyfin.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Install_Fail</td>
    <td>Triggered when the moneyfin installation process encounters an error and fails to complete.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Repair_Cancel</td>
    <td>Triggered when a moneyfin repair operation is cancelled by the user before completion.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Repair_Fail</td>
    <td>Triggered when the moneyfin repair operation fails to complete successfully due to an error.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Runner_Launch</td>
    <td>Indicates when the moneyfin Runner is launched.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.SettingsBootEvent</td>
    <td>Triggered when moneyfin settings are initialized at startup.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.SettingsEnabledEvent</td>
    <td>Indicates that the moneyfin settings have been enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ScoobeStartedEvent</td>
    <td>Triggered when SCOOBE (Secondary Out-of-box experience) starts.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ShortcutConflictControlClickedEvent</td>
    <td>Triggered when a user clicks on the Shortcut Conflict Control button in the moneyfin Settings UI Dashboard.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ShortcutConflictDetectedEvent</td>
    <td>Triggered when keyboard shortcut conflicts are detected in the moneyfin Settings UI Dashboard.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ShortcutConflictResolvedEvent</td>
    <td>Triggered when a keyboard shortcut conflict is resolved in the moneyfin Settings UI.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.TrayFlyoutActivatedEvent</td>
    <td>Indicates when the tray flyout menu is activated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.TrayFlyoutModuleRunEvent</td>
    <td>Logs when a utility from the tray flyout menu is run.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.UnInstall_Cancel</td>
    <td>Triggered when the moneyfin uninstallation process is cancelled by the user before completion.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.UnInstall_Fail</td>
    <td>Triggered when the moneyfin uninstallation process fails to complete successfully due to an error. </td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Uninstall_Success</td>
    <td>Logs when moneyfin is successfully uninstalled (who would do such a thing!).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.UpdateCheck_Completed</td>
    <td>Logs when an auto-update check completes, including success status, whether an update is available, and version information.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.UpdateDownload_Completed</td>
    <td>Logs when an update download completes, including success status and version.</td>
  </tr>
</table>

### OOBE (Out-of-box experience)
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.OobeModuleRunEvent</td>
    <td>Triggered when a user clicks to run or launch a moneyfin module directly from the OOBE (out-of-box experience) interface.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.OobeSectionEvent</td>
    <td>Occurs when OOBE is shown to the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.OobeSettingsEvent</td>
    <td>Triggers when a Settings page is opened from an OOBE page.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.OobeStartedEvent</td>
    <td>Indicates when the out-of-box experience has been initiated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.OobeVariantAssignmentEvent</td>
    <td>This event logs A/B testing assignments for experimental features, helping track which users are in control or alternate groups for feature experiments. </td>
  </tr>
</table>

### Advanced Paste
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPaste_EnableAdvancedPaste</td>
    <td>Triggered when Advanced Paste is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPaste_Error</td>
    <td>Occurs when an error is encountered during the Advanced Paste process.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPaste_InvokeAdvancedPaste</td>
    <td>Activated when Advanced Paste is called by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPaste_Settings</td>
    <td>Triggered when settings for Advanced Paste are accessed or modified.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteClipboardItemClicked</td>
    <td>Occurs when a clipboard item is selected from the Advanced Paste menu.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteClipboardItemDeletedEvent</td>
    <td>Triggered when an item is removed from the Advanced Paste clipboard history.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteCustomFormatOutputThumbUpDownEvent</td>
    <td>Triggered when a user gives feedback on a custom format output (thumb up/down).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteFormatClickedEvent</td>
    <td>Occurs when a specific paste format is clicked in the Advanced Paste menu.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteGenerateCustomErrorEvent</td>
    <td>Triggered when an error occurs while generating a custom paste format.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteGenerateCustomFormatEvent</td>
    <td>Occurs when a custom paste format is successfully generated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteInAppKeyboardShortcutEvent</td>
    <td>Triggered when a keyboard shortcut is used within the Advanced Paste interface.</td>
  </tr>  
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteSemanticKernelFormatEvent</td>
    <td>Triggered when Advanced Paste leverages the Semantic Kernel.</td>
  </tr> 
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteSemanticKernelErrorEvent</td>
    <td>Occurs when the Semantic Kernel workflow encounters an error.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteEndpointUsageEvent</td>
    <td>Logs the AI provider, model, and processing duration for each endpoint call.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AdvancedPasteCustomActionErrorEvent</td>
    <td>Records provider, model, and status details when a custom action fails.</td>
  </tr>
</table>

### Always on Top
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AlwaysOnTop_EnableAlwaysOnTop</td>
    <td>Triggered when Always on Top is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AlwaysOnTop_PinWindow</td>
    <td>Occurs when a window is pinned to stay on top of other windows.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AlwaysOnTop_UnpinWindow</td>
    <td>Triggered when a pinned window is unpinned, allowing it to be behind other windows.</td>
  </tr>
</table>

### Awake
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Awake_EnableAwake</td>
    <td>Triggered when Awake is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AwakeExpirableKeepAwakeEvent</td>
    <td>Occurs when the system is kept awake for a temporary, expirable duration.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AwakeIndefinitelyKeepAwakeEvent</td>
    <td>Triggered when the system is set to stay awake indefinitely.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AwakeNoKeepAwakeEvent</td>
    <td>Occurs when Awake is turned off, allowing the computer to enter sleep mode.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.AwakeTimedKeepAwakeEvent</td>
    <td>Triggered when the system is kept awake for a specified time duration.</td>
  </tr>  
</table>

### Color Picker
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ColorPicker_EnableColorPicker</td>
    <td>Triggered when Color Picker is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ColorPicker_Session</td>
    <td>Occurs during a Color Picker usage session.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ColorPicker_Settings</td>
    <td>Triggered when the settings for the Color Picker are accessed or modified.</td>
  </tr>
</table>

### Command Not Found
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdNotFound_EnableCmdNotFound</td>
    <td>Triggered when Command Not Found is enabled or disabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdNotFoundInstallEvent</td>
    <td>Triggered when a Command Not Found is installed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdNotFoundUninstallEvent</td>
    <td>Triggered when Command Not Found is uninstalled after being previously installed.</td>
  </tr>  
</table>

### Command Palette

<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_BeginInvoke</td>
    <td>Triggered when the Command Palette is launched by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_ColdLaunch</td>
    <td>Occurs when Command Palette starts for the first time (cold start).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_OpenPage</td>
    <td>Triggered when a page is opened within the Command Palette, tracking navigation depth.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_OpenUri</td>
    <td>Occurs when a URI is opened through the Command Palette, including whether it's a web URL.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_ReactivateInstance</td>
    <td>Triggered when an existing Command Palette instance is reactivated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_RunCommand</td>
    <td>Logs when a command is executed through the Command Palette, including admin elevation status.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_RunQuery</td>
    <td>Triggered when a search query is performed, including result count and duration.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPalDismissedOnEsc</td>
    <td>Occurs when the Command Palette is dismissed by pressing the Escape key.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPalDismissedOnLostFocus</td>
    <td>Triggered when the Command Palette is dismissed due to losing focus.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPalHotkeySummoned</td>
    <td>Logs when the Command Palette is summoned via hotkey, distinguishing between global and context-specific hotkeys.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPalInvokeResult</td>
    <td>Records the result type of a Command Palette invocation.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPalProcessStarted</td>
    <td>Triggered when the Command Palette process is started.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_ExtensionInvoked</td>
    <td>Tracks extension usage including extension ID, command details, success status, and execution time.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CmdPal_SessionDuration</td>
    <td>Logs session metrics from launch to dismissal including duration, commands executed, pages visited, search queries, navigation depth, and errors.</td>
  </tr>
</table>

### Crop And Lock
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_ActivateReparent</td>
    <td>Triggered when the cropping interface is activated for reparenting the cropped content.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_ActivateScreenshot</td>
    <td>Triggered when the screenshot mode is activated in Crop and Lock.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_ActivateThumbnail</td>
    <td>Occurs when the thumbnail view for cropped content is activated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_CreateReparentWindow</td>
    <td>Triggered when a reparent window is created in Crop and Lock mode.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_CreateScreenshotWindow</td>
    <td>Triggered when a screenshot window is created in Crop and Lock mode.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_CreateThumbnailWindow</td>
    <td>Triggered when a thumbnail window is created in Crop and Lock mode.<-/td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_EnableCropAndLock</td>
    <td>Triggered when Crop and Lock is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CropAndLock_Settings</td>
    <td>Occurs when settings related to Crop and Lock are modified.</td>
  </tr>  
</table>

### Cursor Wrap
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.CursorWrap_EnableCursorWrap</td>
    <td>Triggered when Cursor Wrap is enabled or disabled.</td>
  </tr>
</table>

### Environment Variables
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.EnvironmentVariables_Activate</td>
    <td>Triggered when Environment Variables is launched.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.EnvironmentVariables_EnableEnvironmentVariables</td>
    <td>Occurs when Environment Variables is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.EnvironmentVariablesOpenedEvent</td>
    <td>Triggered when the Environment Variables interface is opened.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.EnvironmentVariablesProfileEnabledEvent</td>
    <td>Occurs when an environment variable profile is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.EnvironmentVariablesVariableChangedEvent</td>
    <td>Triggered when an environment variable is added, modified, or deleted.</td>
  </tr>  
</table>

### FancyZones
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_CycleActiveZoneSet</td>
    <td>Triggered when the active zone set is cycled through.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_EditorLaunch</td>
    <td>Occurs when the FancyZones editor is launched.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_EnableFancyZones</td>
    <td>Occurs when FancyZones is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_Error</td>
    <td>Triggered when an error occurs within the FancyZones module. This event logs critical errors to help diagnose and troubleshoot issues with FancyZones functionality, such as failures to set up Windows hooks or other system-level operations required for window management.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_KeyboardSnapWindowToZone</td>
    <td>Triggered when a window is snapped to a zone using the keyboard.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_MoveOrResizeEnded</td>
    <td>Occurs when a window move or resize action has completed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_MoveOrResizeStarted</td>
    <td>Triggered when a window move or resize action is initiated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_OnKeyDown</td>
    <td>Triggered when a key is pressed down while interacting with zones.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_QuickLayoutSwitch</td>
    <td>Occurs when a quick switch between zone layouts is performed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_Settings</td>
    <td>Triggered when FancyZones settings are accessed or modified.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_SnapNewWindowIntoZone</td>
    <td>Triggered when a new window is snapped into a zone.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_VirtualDesktopChanged</td>
    <td>Occurs when the virtual desktop changes, affecting zone layout.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_ZoneSettingsChanged</td>
    <td>Triggered when the settings for specific zones are altered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_ZoneWindowKeyUp</td>
    <td>Occurs when a key is released while interacting with zones.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZones_CLICommand</td>
    <td>Triggered when a FancyZones CLI command is executed, logging the command name and success status.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZonesEditorStartEvent</td>
    <td>Triggered when the FancyZones Editor application starts. This logs the initialization of the editor UI, which is used to create and configure custom zone layouts.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FancyZonesEditorStartFinishEvent</td>
    <td>Triggered when the FancyZones Editor has completed loading and is ready for user interaction.</td>
  </tr>
</table>

### File Locksmith
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FileLocksmith_EnableFileLocksmith</td>
    <td>Triggered when File Locksmith is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FileLocksmith_Invoked</td>
    <td>Occurs when File Locksmith is invoked.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FileLocksmith_InvokedRet</td>
    <td>Triggered when File Locksmith invocation returns a result.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FileLocksmith_QueryContextMenuError</td>
    <td>Occurs when there is an error querying the context menu for File Locksmith.</td>
  </tr>
</table>

### FileExplorerAddOns
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.GcodeFileHandlerLoaded</td>
    <td>Triggered when a G-code file handler is loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.GcodeFilePreviewed</td>
    <td>Occurs when a G-code file is previewed in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.GcodeFilePreviewError</td>
    <td>Triggered when there is an error previewing a G-code file.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.BgcodeFileHandlerLoaded</td>
    <td>Triggered when a Binary G-code file handler is loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.BgcodeFilePreviewed</td>
    <td>Occurs when a Binary G-code file is previewed in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.BgcodeFilePreviewError</td>
    <td>Triggered when there is an error previewing a Binary G-code file.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MarkdownFileHandlerLoaded</td>
    <td>Occurs when a Markdown file handler is loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MarkdownFilePreviewed</td>
    <td>Triggered when a Markdown file is previewed in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MarkdownFilePreviewError</td>
    <td>Triggered when there is an error previewing a Markdown file in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PdfFileHandlerLoaded</td>
    <td>Occurs when a PDF file handler is loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PdfFilePreviewed</td>
    <td>Triggered when a PDF file is previewed in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PdfFilePreviewError</td>
    <td>Triggered when there is an error previewing a PDF file in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerPreview_Enabled</td>
    <td>Occurs when preview is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerPreview_TweakUISettings_Destroyed</td>
    <td>Triggered when the Tweak UI settings for Power Preview are destroyed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerPreview_TweakUISettings_FailedUpdatingSettings</td>
    <td>Occurs when updating Tweak UI settings fails.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerPreview_TweakUISettings_InitSet__ErrorLoadingFile</td>
    <td>Triggered when there is an error loading a file during Tweak UI settings initialization.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerPreview_TweakUISettings_SetConfig__InvalidJSONGiven</td>
    <td>Triggered when invalid JSON is provided to the Power Preview settings configuration</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerPreview_TweakUISettings_SuccessfullyUpdatedSettings</td>
    <td>Occurs when the Tweak UI settings for Power Preview are successfully updated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.QoiFilePreviewed</td>
    <td>Triggered when a QOI file is previewed in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.QoiFilePreviewError</td>
    <td>Triggered when there is an error previewing a QOI (Quite OK Image) file in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.SvgFileHandlerLoaded</td>
    <td>Occurs when an SVG file handler is loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.SvgFilePreviewed</td>
    <td>Triggered when an SVG file is previewed in File Explorer.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.SvgFilePreviewError</td>
    <td>Occurs when there is an error previewing an SVG file.</td>
  </tr>
</table>

### Find My Mouse
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FindMyMouse_EnableFindMyMouse</td>
    <td>Triggered when Find My Mouse is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.FindMyMouse_MousePointerFocused</td>
    <td>Occurs when the mouse pointer is focused using Find My Mouse, including the activation method (double-tap left/right Ctrl, shake mouse, or shortcut).</td>
  </tr>
</table>

### Hosts File Editor
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.HostsFileEditor_Activate</td>
    <td>Triggered when Hosts File Editor is activated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.HostsFileEditor_EnableHostsFileEditor</td>
    <td>Occurs when Hosts File Editor is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.HostsFileEditorOpenedEvent</td>
    <td>Fires when Hosts File Editor is opened.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.HostEditorStartEvent</td>
    <td>Triggered when the Hosts File Editor application starts. This logs the initialization of the Hosts File Editor UI with a timestamp.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.HostEditorStartFinishEvent</td>
    <td>Triggered when the Hosts File Editor has completed loading and is ready for user interaction.</td>
  </tr>
</table>

### Image Resizer
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ImageResizer_EnableImageResizer</td>
    <td>Triggered when Image Resizer is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ImageResizer_Invoked</td>
    <td>Occurs when Image Resizer is invoked by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ImageResizer_InvokedRet</td>
    <td>Fires when the Image Resizer operation is completed and returns a result.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ImageResizer_QueryContextMenuError</td>
    <td>Triggered when there is an error querying the context menu for Image Resizer.</td>
  </tr>
</table>

### Keyboard Manager
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_AppSpecificShortcutRemapConfigurationLoaded</td>
    <td>Indicates that the application-specific shortcut remap configuration has been successfully loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_AppSpecificShortcutRemapCount</td>
    <td>Logs the number of application-specific shortcut remaps configured by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_AppSpecificShortcutToKeyRemapInvoked</td>
    <td>Logs each instance when an application-specific shortcut-to-key remap is used.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_AppSpecificShortcutToShortcutRemapInvoked</td>
    <td>Logs each instance when an application-specific shortcut-to-shortcut remap is used.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_Error</td>
    <td>Triggered when an error occurs in Keyboard Manager. This logs the error code, error message, and the method name where the error occurred.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_ErrorSendingKeyAndShortcutRemapLoadedConfiguration</td>
    <td>Triggered when there is an error sending remapping configuration telemetry. This occurs when Keyboard Manager fails to report the loaded key and shortcut remap configurations</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_DailyAppSpecificShortcutToKeyRemapInvoked</td>
    <td>Logs the daily count of application-specific shortcut-to-key remaps executed by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_DailyAppSpecificShortcutToShortcutRemapInvoked</td>
    <td>Logs the daily count of application-specific shortcut-to-shortcut remaps executed by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_DailyKeyToKeyRemapInvoked</td>
    <td>Logs the daily count of key-to-key remaps used by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_DailyKeyToShortcutRemapInvoked</td>
    <td>Logs the daily count of key-to-shortcut remaps used by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_DailyShortcutToKeyRemapInvoked</td>
    <td>Logs the daily count of shortcut-to-key remaps used by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_DailyShortcutToShortcutRemapInvoked</td>
    <td>Logs the daily count of shortcut-to-shortcut remaps used by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_EnableKeyboardManager</td>
    <td>Indicates that the Keyboard Manager has been enabled in moneyfin settings.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_KeyRemapConfigurationLoaded</td>
    <td>Indicates that the key remap configuration has been successfully loaded.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_KeyRemapCount</td>
    <td>Logs the number of individual key remaps configured by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_KeyToKeyRemapInvoked</td>
    <td>Logs each instance of a key-to-key remap being used.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_KeyToShortcutRemapInvoked</td>
    <td>Logs each instance of a key-to-shortcut remap being used.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_OSLevelShortcutRemapCount</td>
    <td>Logs the total number of OS-level shortcut remaps configured by the user.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_OSLevelShortcutToKeyRemapInvoked</td>
    <td>Logs each instance of an OS-level shortcut-to-key remap being used.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_OSLevelShortcutToShortcutRemapInvoked</td>
    <td>Logs each instance of an OS-level shortcut-to-shortcut remap being used.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.KeyboardManager_ShortcutRemapConfigurationLoaded</td>
    <td>Indicates that the shortcut remap configuration has been successfully loaded.</td>
  </tr>
</table>

### Light Switch
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LightSwitch_EnableLightSwitch</td>
    <td>Triggered when Light Switch is enabled or disabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LightSwitch_ShortcutInvoked</td>
    <td>Occurs when the shortcut for Light Switch is invoked.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LightSwitch_ScheduleModeToggled</td>
    <td>Occurs when a new schedule mode is selected for Light Switch.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LightSwitch_ThemeTargetChanged</td>
    <td>Occurs when the options for targeting the system or apps is updated.</td>
  </tr>
</table>

### Mouse Highlighter
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseHighlighter_EnableMouseHighlighter</td>
    <td>Triggered when Mouse Highlighter is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseHighlighter_StartHighlightingSession</td>
    <td>Occurs when a new highlighting session is started.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseHighlighter_StartSpotlightSession</td>
    <td>Triggered when a spotlight session is started in Mouse Highlighter. This occurs when the user activates the spotlight mode.</td>
  </tr>
</table>

### Mouse Jump
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseJump_EnableJumpTool</td>
    <td>Triggered when Mouse Jump is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseJump_InvokeJumpTool</td>
    <td>Occurs when Mouse Jump is invoked.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseJumpShowEvent</td>
    <td>Triggered when the Mouse Jump display is shown.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseJumpTeleportCursorEvent</td>
    <td>Occurs when the cursor is teleported to a new location.</td>
  </tr>
</table>

### Mouse Pointer Crosshairs
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MousePointerCrosshairs_EnableMousePointerCrosshairs</td>
    <td>Triggered when Mouse Pointer Crosshairs is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MousePointerCrosshairs_StartDrawingCrosshairs</td>
    <td>Occurs when the crosshairs are drawn around the mouse pointer.</td>
  </tr>
</table>

### Mouse Without Borders
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBorders_Activate</td>
    <td>Triggered when Mouse Without Borders is activated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBorders_AddFirewallRule</td>
    <td>Occurs when a firewall rule is added for Mouse Without Borders.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBorders_EnableMouseWithoutBorders</td>
    <td>Triggered when Mouse Without Borders is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBorders_ToggleServiceRegistration</td>
    <td>Occurs when the service registration for Mouse Without Borders is toggled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersClipboardFileTransferEvent</td>
    <td>Triggered during a clipboard file transfer between computers.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersDragAndDropEvent</td>
    <td>Occurs during a drag-and-drop operation between computers.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersMultipleModeEvent</td>
    <td>Triggered when multiple modes are enabled in Mouse Without Borders.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersOldUIOpenedEvent</td>
    <td>Occurs when the old user interface for Mouse Without Borders is opened.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersOldUIQuitEvent</td>
    <td>Triggered when the old user interface for Mouse Without Borders is closed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersOldUIReconfigureEvent</td>
    <td>Occurs when the old user interface for Mouse Without Borders is reconfigured.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MouseWithoutBordersStartedEvent</td>
    <td>Triggered when Mouse Without Borders is started.</td>
  </tr>
</table>

### New+
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.NewPlus_ChangedTemplateLocation</td>
    <td>Triggered when the template folder location is changed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.NewPlus_EventCopyTemplate</td>
    <td>Triggered when an item from New+ is created (copied to the current directory).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.NewPlus_EventCopyTemplateResult</td>
    <td>Logs the success of item creation (copying).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.NewPlus_EventOpenTemplates</td>
    <td>Triggered when the templates folder is opened.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.NewPlus_EventShowTemplateItems</td>
    <td>Triggered when the New+ context menu flyout is displayed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.NewPlus_EventToggleOnOff</td>
    <td>Triggered when New+ is enabled or disabled.</td>
  </tr>
</table>

### Peek
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_Closed</td>
    <td>Triggered when Peek is closed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_EnablePeek</td>
    <td>Occurs when Peek is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_Error</td>
    <td>Triggered when an error occurs for Peek.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_InvokePeek</td>
    <td>Occurs when Peek is invoked.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_Opened</td>
    <td>Triggered when a Peek window is opened.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_OpenWith</td>
    <td>Occurs when an item is opened with Peek.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_Settings</td>
    <td>Triggered when the settings for Peek are modified.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Peek_SpaceModeEnabled</td>
    <td>Triggered when the Space key activation mode is enabled or disabled in Peek</td>
  </tr>
</table>

### PowerRename
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerRename_EnablePowerRename</td>
    <td>Triggered when PowerRename is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerRename_Invoked</td>
    <td>Occurs when PowerRename is invoked.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerRename_InvokedRet</td>
    <td>Triggered when the invocation of PowerRename returns a result.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerRename_RenameOperation</td>
    <td>Triggered during the rename operation within PowerRename.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerRename_SettingsChanged</td>
    <td>Occurs when the settings for PowerRename are changed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerRename_UIShownRet</td>
    <td>Triggered when the PowerRename user interface is shown.</td>
  </tr>
</table>

### moneyfin Run
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherBootEvent</td>
    <td>Triggered when moneyfin Run is initialized on boot.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherColdStateHotkeyEvent</td>
    <td>Occurs when the hotkey is pressed in the cold state (not yet initialized).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherFirstDeleteEvent</td>
    <td>Triggered when the first deletion action is performed in moneyfin Run.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherHideEvent</td>
    <td>Occurs when moneyfin Run is hidden.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherQueryEvent</td>
    <td>Triggered when a query is made in moneyfin Run.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherResultActionEvent</td>
    <td>Occurs when an action is taken on a result in moneyfin Run.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherShowEvent</td>
    <td>Triggered when moneyfin Run is shown.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.LauncherWarmStateHotkeyEvent</td>
    <td>Occurs when the hotkey is pressed in the warm state (initialized).</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.RunPluginsSettingsEvent</td>
    <td>Triggered when the settings for moneyfin Run plugins are accessed or modified.</td>
  </tr>
</table>

### Quick Accent
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerAccent_EnablePowerAccent</td>
    <td>Triggered when Quick Accent is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerAccentShowAccentMenuEvent</td>
    <td>Occurs when the accent menu is displayed.</td>
  </tr>
</table>

### Registry Preview
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.RegistryPreview_Activate</td>
    <td>Triggered when Registry Preview is activated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.RegistryPreview_EnableRegistryPreview</td>
    <td>Occurs when Registry Preview is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.RegistryPreviewEditorStartEvent</td>
    <td>Triggered when the Registry Preview application starts. This logs the initialization of the Registry Preview UI with a timestamp.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.RegistryPreviewEditorStartFinishEvent</td>
    <td>Triggered when the Registry Preview application has completed loading and is ready for user interaction.</td>
  </tr>
</table>

### Screen Ruler
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MeasureTool_BoundsToolActivated</td>
    <td>Triggered when Screen Ruler's Bounds tool is activated.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MeasureTool_EnableMeasureTool</td>
    <td>Occurs when Screen Ruler is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.MeasureTool_MeasureToolActivated</td>
    <td>Triggered when Screen Ruler's Measure tool is activated.</td>
  </tr>
</table>

### Shortcut Guide
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ShortcutGuide_GuideSession</td>
    <td>Logs a Shortcut Guide session including duration and how it was closed.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ShortcutGuide_Settings</td>
    <td>Indicates a change in the settings related to the Shortcut Guide.</td>
  </tr>
</table>

### Text Extractor
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerOCR_EnablePowerOCR</td>
    <td>Triggered when the Text Extractor (OCR) feature is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerOCRCancelledEvent</td>
    <td>Occurs when the text extraction process is cancelled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerOCRCaptureEvent</td>
    <td>Occurs when the user has created a capture for text extraction.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.PowerOCRInvokedEvent</td>
    <td>Triggered when Text Extractor is invoked.</td>
  </tr>
</table>

### Workspaces
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Workspaces_CreateEvent</td>
    <td>Triggered when a new workspace is created.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Workspaces_DeleteEvent</td>
    <td>Triggered when a workspace is deleted.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Workspaces_EditEvent</td>
    <td>Triggered when a workspace is edited or modified.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Workspaces_Enable</td>
    <td>Indicates that Workspaces is enabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.Workspaces_LaunchEvent</td>
    <td>Triggered when a workspace is launched.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.WorkspacesEditorStartEvent</td>
    <td>Triggered when the Workspaces Editor application starts. This logs the initialization of the Workspaces Editor UI with a timestamp.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.WorkspacesEditorStartFinishEvent</td>
    <td>Triggered when the Workspaces Editor has completed loading and is ready for user interaction.</td>
  </tr>
</table>

### ZoomIt
<table style="width:100%; table-layout:fixed">
  <colgroup>
    <col style="width:40%">
    <col style="width:60%">
  </colgroup>
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_EnableZoomIt</td>
    <td>Triggered when ZoomIt is enabled/disabled.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_Started</td>
    <td>Triggered when the ZoomIt process starts.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateBreak</td>
    <td>Triggered when the Break mode is entered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateDraw</td>
    <td>Triggered when the Draw mode is entered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateZoom</td>
    <td>Triggered when the Zoom mode is entered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateLiveZoom</td>
    <td>Triggered when the Live Zoom mode is entered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateDemoType</td>
    <td>Triggered when the DemoType mode is entered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateRecord</td>
    <td>Triggered when the Record mode is entered.</td>
  </tr>
  <tr>
    <td>Microsoft.moneyfin.ZoomIt_ActivateSnip</td>
    <td>Triggered when the Snip mode is entered.</td>
  </tr>
</table>

<!-- back up of table

<table style="width:100%">
  <tr>
    <th>Event Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td>x</td>
    <td>x</td>
  </tr>
</table>
-->
