# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.frontpage -t test_item.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.frontpage.testing.COLLECTIVE_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/frontpage/tests/robot/test_item.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Item
  Given a logged-in site administrator
    and an add Item form
   When I type 'My Item' into the title field
    and I submit the form
   Then a Item with the title 'My Item' has been created

Scenario: As a site administrator I can view a Item
  Given a logged-in site administrator
    and a Item 'My Item'
   When I go to the Item view
   Then I can see the Item title 'My Item'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Item form
  ${uid} =  Create content  type=Frontpage  id=my-frontpage  title=My Frontpage
  Create content  type=Section  container=${uid}  id=my-section  title=My Section
  Go To  ${PLONE_URL}/my-frontpage/my-section/++add++Item

a Item 'My Item'
  ${uid} =  Create content  type=Frontpage  id=my-frontpage  title=My Frontpage
  ${uid} =  Create content  type=Section  container=${uid}  id=my-section  title=My Section
  Create content  type=Item  container=${uid}  id=my-item  title=My Item

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Item view
  Go To  ${PLONE_URL}/my-frontpage/my-section/my-item
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Item with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Item title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
