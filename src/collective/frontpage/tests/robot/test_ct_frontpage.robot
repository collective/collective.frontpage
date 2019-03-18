# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.frontpage -t test_frontpage.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.frontpage.testing.COLLECTIVE_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/frontpage/tests/robot/test_frontpage.robot
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

Scenario: As a site administrator I can add a Frontpage
  Given a logged-in site administrator
    and an add Frontpage form
   When I type 'My Frontpage' into the title field
    and I submit the form
   Then a Frontpage with the title 'My Frontpage' has been created

Scenario: As a site administrator I can view a Frontpage
  Given a logged-in site administrator
    and a Frontpage 'My Frontpage'
   When I go to the Frontpage view
   Then I can see the Frontpage title 'My Frontpage'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Frontpage form
  Go To  ${PLONE_URL}/++add++Frontpage

a Frontpage 'My Frontpage'
  Create content  type=Frontpage  id=my-frontpage  title=My Frontpage

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Frontpage view
  Go To  ${PLONE_URL}/my-frontpage
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Frontpage with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Frontpage title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
